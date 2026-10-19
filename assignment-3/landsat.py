"""
Landsat 8 raster analysis with rasterio.

Assignment 3 — Unit 4: Rasterio
"""

import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.enums import Resampling
from rasterio import transform
from rasterio.warp import calculate_default_transform, reproject


# ---------------------------------------------------------------------------
# Configuration — the course Landsat 8 bands from gist415-landsat.zip (D2L),
# unzipped into data/ in this repository. Full paths, so the script works
# whichever folder it is run from.
# ---------------------------------------------------------------------------
DATA = '/home/jovyan/work/data/landsat/'
SCENE = 'LC08_L1TP_042034_20170616_20170629_01_T1'   # 16 June 2017
OUT = '/home/jovyan/work/assignment-3/'

BAND_3 = DATA + SCENE + '_B3.TIF'   # Green
BAND_4 = DATA + SCENE + '_B4.TIF'   # Red
BAND_5 = DATA + SCENE + '_B5.TIF'   # NIR
BAND_6 = DATA + SCENE + '_B6.TIF'   # SWIR


# ---------------------------------------------------------------------------
# Helper — read a band as float32, with decimation for overviews
# ---------------------------------------------------------------------------
def read_band(path, decimation=1):
    """Read a single-band raster, optionally decimated."""
    with rasterio.open(path) as src:
        data = src.read(
            1,
            out_shape=(
                1,
                int(src.height / decimation),
                int(src.width / decimation),
            ),
            resampling=Resampling.average,
        ).astype('float32')
        profile = src.profile
    return data, profile


# ---------------------------------------------------------------------------
# NDVI
# ---------------------------------------------------------------------------
def calc_ndvi(nir, red):
    """NDVI = (NIR - Red) / (NIR + Red)"""
    nir = nir.astype('float32')
    red = red.astype('float32')
    with np.errstate(divide='ignore', invalid='ignore'):
        ndvi = np.where(
            (nir + red) == 0,
            np.nan,
            (nir - red) / (nir + red)
        )
    return ndvi


# ---------------------------------------------------------------------------
# Q6 — mNDWI (Modified Normalized Difference Water Index)
# ---------------------------------------------------------------------------
def calc_mndwi(green, swir):
    """mNDWI = (Green - SWIR) / (Green + SWIR)"""
    pass  # replace with your implementation


# ---------------------------------------------------------------------------
# Q10 — Reprojection to California State Plane Zone 3 (EPSG:2227)
# ---------------------------------------------------------------------------
def reproject_to_epsg2227(src_path, dst_path):
    """Reproject a raster to EPSG:2227 and write it to dst_path."""
    target_crs = 'EPSG:2227'

    with rasterio.open(src_path) as src:
        dst_transform_calc, dst_width, dst_height = calculate_default_transform(
            src.crs, target_crs, src.width, src.height, *src.bounds
        )
        dst_profile = src.profile.copy()
        dst_profile.update({
            'crs': target_crs,
            'transform': dst_transform_calc,
            'width': dst_width,
            'height': dst_height,
        })

        with rasterio.open(dst_path, 'w', **dst_profile) as dst:
            for i in range(1, src.count + 1):
                reproject(
                    source=rasterio.band(src, i),
                    destination=rasterio.band(dst, i),
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=dst_transform_calc,
                    dst_crs=target_crs,
                    resampling=Resampling.bilinear,
                )
    print(f'Reprojected → {dst_path}  ({dst_width}×{dst_height} pixels)')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    DECIMATION = 4  # read at 1/4 resolution for speed

    print('Reading bands...')
    green, profile = read_band(BAND_3, DECIMATION)
    red, _ = read_band(BAND_4, DECIMATION)
    nir, _ = read_band(BAND_5, DECIMATION)
    swir, _ = read_band(BAND_6, DECIMATION)

    # Mask NoData (0 values → NaN)
    for arr in [green, red, nir, swir]:
        arr[arr == 0] = np.nan

    # --- NDVI ---
    ndvi = calc_ndvi(nir, red)

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.colorbar(im, ax=ax, label='NDVI')
    ax.set_title('NDVI')
    ax.set_axis_off()
    plt.tight_layout()
    plt.savefig(OUT + 'ndvi.png', dpi=150)
    plt.show()

    # --- NDVI difference (Q9) ---
    # Add your standalone NDVI difference plot (2018 minus 2017) here, with a
    # colormap not used in the tutorial and a colorbar, and save it as
    # OUT + 'screencap_ndvi_difference.png'.

    # --- mNDWI (Q6) ---
    mndwi = calc_mndwi(green, swir)
    if mndwi is not None:
        fig, ax = plt.subplots(figsize=(8, 6))
        im = ax.imshow(mndwi, cmap='Blues', vmin=-1, vmax=1)
        plt.colorbar(im, ax=ax, label='mNDWI')
        ax.set_title('mNDWI (Modified Normalized Difference Water Index)')
        ax.set_axis_off()
        plt.tight_layout()
        plt.savefig(OUT + 'screencap_mndwi.png', dpi=150)
        plt.show()

    # --- Reprojection (Q10) ---
    reproject_to_epsg2227(BAND_5, OUT + 'nir_epsg2227.tif')
