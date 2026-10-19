#!/usr/bin/env python
"""Quick test of the GIST 415 Python environment.

Each check does a small piece of real work with one library, using data it makes
itself, so it needs no internet and no course files. Takes well under a minute.

Run it inside the course container:
    docker compose run --rm jupyter check-environment
or from a notebook cell:
    !check-environment
"""

import sys
import tempfile
import traceback
from pathlib import Path

results = []


def check(name):
    """Run the decorated function as a named check and record pass/fail."""
    def wrap(fn):
        try:
            detail = fn()
            results.append((True, name, detail or ""))
        except Exception as exc:  # report every failure, keep going
            results.append((False, name, f"{type(exc).__name__}: {exc}"))
            traceback.print_exc(file=sys.stderr)
        return fn
    return wrap


# Tucson, used throughout: longitude, latitude in WGS 84 and UTM zone 12N (EPSG:26912).
LON, LAT = -110.97, 32.22


@check("pandas: group and aggregate")
def _():
    import pandas as pd
    df = pd.DataFrame({"ward": [1, 1, 2, 2, 2], "lights": [3, 5, 2, 4, 6]})
    totals = df.groupby("ward")["lights"].sum()
    assert totals.to_dict() == {1: 8, 2: 12}, totals
    return f"pandas {pd.__version__}"


@check("numpy: array math")
def _():
    import numpy as np
    a = np.arange(6, dtype="float32").reshape(2, 3)
    assert float(a.mean()) == 2.5
    return f"numpy {np.__version__}"


@check("matplotlib: draw and save a figure")
def _():
    import io
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4])
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    assert buf.tell() > 1000
    return f"matplotlib {matplotlib.__version__}"


@check("shapely: geometry (GEOS)")
def _():
    import shapely
    from shapely.geometry import Point
    area = Point(0, 0).buffer(10).area
    assert 310 < area < 315, area  # close to pi * 10^2
    return f"shapely {shapely.__version__}, GEOS {shapely.geos_version_string}"


@check("pyproj: WGS 84 to UTM 12N (PROJ)")
def _():
    import pyproj
    to_utm = pyproj.Transformer.from_crs(4326, 26912, always_xy=True)
    x, y = to_utm.transform(LON, LAT)
    assert 400_000 < x < 600_000 and 3_400_000 < y < 3_700_000, (x, y)
    return f"pyproj {pyproj.__version__}, PROJ {pyproj.proj_version_str}"


def sample_layers():
    """Two small layers in WGS 84: square zones and points, one point per zone plus one outside."""
    import geopandas as gpd
    from shapely.geometry import Point, box
    zones = gpd.GeoDataFrame(
        {"zone": ["A", "B"]},
        geometry=[box(LON - 0.02, LAT - 0.01, LON, LAT + 0.01),
                  box(LON, LAT - 0.01, LON + 0.02, LAT + 0.01)],
        crs="EPSG:4326",
    )
    points = gpd.GeoDataFrame(
        {"value": [10, 20, 30]},
        geometry=[Point(LON - 0.01, LAT), Point(LON + 0.01, LAT), Point(LON + 0.5, LAT)],
        crs="EPSG:4326",
    )
    return zones, points


@check("geopandas: reproject, write and read a GeoPackage, spatial join")
def _():
    import geopandas as gpd
    zones, points = sample_layers()
    zones_utm = zones.to_crs(26912)
    assert zones_utm.crs.to_epsg() == 26912
    assert 3_500_000 < zones_utm.area.sum() < 9_000_000, zones_utm.area.sum()  # about 2 x 1.9 km x 2.2 km
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "zones.gpkg"
        zones.to_file(path, layer="zones", driver="GPKG")
        back = gpd.read_file(path, layer="zones")
    assert len(back) == 2 and back.crs.to_epsg() == 4326
    joined = gpd.sjoin(points, zones, predicate="within", how="inner")
    assert sorted(joined["zone"]) == ["A", "B"], joined
    import pyogrio
    return f"geopandas {gpd.__version__}, pyogrio {pyogrio.__version__}"


def sample_raster():
    """A 2-band 10 x 10 raster (red, near infrared) in UTM 12N with 30 m cells."""
    import numpy as np
    from rasterio.transform import from_origin
    red = np.full((10, 10), 0.1, dtype="float32")
    nir = np.full((10, 10), 0.5, dtype="float32")
    transform = from_origin(500_000, 3_566_000, 30, 30)
    return red, nir, transform


@check("rasterio: write and read a GeoTIFF, NDVI (GDAL)")
def _():
    import numpy as np
    import rasterio
    from rasterio.io import MemoryFile
    red, nir, transform = sample_raster()
    with MemoryFile() as mem:
        with mem.open(driver="GTiff", height=10, width=10, count=2, dtype="float32",
                      crs="EPSG:26912", transform=transform) as dst:
            dst.write(np.stack([red, nir]))
        with mem.open() as src:
            r, n = src.read(1), src.read(2)
            assert src.crs.to_epsg() == 26912
            row, col = src.index(500_015, 3_565_985)
            assert (row, col) == (0, 0), (row, col)
    ndvi = (n - r) / (n + r)
    assert abs(float(ndvi.mean()) - 0.6667) < 0.001, ndvi.mean()
    return f"rasterio {rasterio.__version__}, GDAL {rasterio.__gdal_version__}"


@check("rasterstats: zonal statistics")
def _():
    import rasterstats
    from shapely.geometry import box
    red, nir, transform = sample_raster()
    zone = box(500_000, 3_565_850, 500_150, 3_566_000)  # top-left 5 x 5 cells
    stats = rasterstats.zonal_stats([zone], nir, affine=transform, nodata=-9999,
                                    stats=["mean", "count"])[0]
    assert stats["count"] == 25 and abs(stats["mean"] - 0.5) < 1e-6, stats
    return f"rasterstats {rasterstats.__version__}"


@check("mapclassify: choropleth classes")
def _():
    import mapclassify
    q = mapclassify.Quantiles([1, 2, 3, 4, 5, 6, 7, 8], k=4)
    assert len(q.bins) == 4, q.bins
    return f"mapclassify {mapclassify.__version__}"


@check("folium: interactive map with GeoDataFrame.explore()")
def _():
    import folium
    zones, _ = sample_layers()
    m = zones.explore(column="zone")
    html = m.get_root().render()
    assert "leaflet" in html.lower()
    return f"folium {folium.__version__}"


@check("jupyterlab: installed")
def _():
    import jupyterlab
    return f"jupyterlab {jupyterlab.__version__}"


# Optional: the GeoPandas tutorial's sample data. Cached in the image; a miss is a warning.
geodatasets_note = ""
try:
    import geodatasets
    geodatasets.get_path("nybb")
    results.append((True, "geodatasets: NYC boroughs sample data", f"geodatasets {geodatasets.__version__}"))
except Exception as exc:
    geodatasets_note = (f"  note: geodatasets could not load the NYC boroughs data ({type(exc).__name__}). "
                        "It downloads on first use, so this only matters offline.")

print()
print(f"GIST 415 environment check (Python {sys.version.split()[0]})")
print("-" * 60)
for ok, name, detail in results:
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}")
    if detail:
        print(f"         {detail}")
if geodatasets_note:
    print(geodatasets_note)
print("-" * 60)
failed = [name for ok, name, _ in results if not ok]
if failed:
    print(f"{len(failed)} check(s) FAILED. Copy this output into a message to the instructor.")
    sys.exit(1)
print(f"All {len(results)} checks passed. The environment is ready.")
