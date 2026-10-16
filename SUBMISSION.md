# Unit 5 — Submission

All of your Unit 5 written answers go in this file. Replace every `_Your answer here._` with your own answer, and commit to your `unit-5-work` branch after each assignment.

Screenshots and other files go in each assignment's `assignment-N/` folder, using the exact file names below. Screenshots then appear in this file automatically when you view it on GitHub.

---

## Assignment 1: GeoPandas Introduction

**Files for this assignment** (add them to `assignment-1/`):

![screencap-workspace-gdf.png](assignment-1/screencap-workspace-gdf.png)

![screencap-gdf-dist.png](assignment-1/screencap-gdf-dist.png)

![screencap-gdf-centroids.png](assignment-1/screencap-gdf-centroids.png)

![screencap-gdf-buffered-centroid.png](assignment-1/screencap-gdf-buffered-centroid.png)

---

## Assignment 2: GeoPandas Spatial Join

**Files for this assignment** (add them to `assignment-2/`):

- [`assignment-2/spatial_join.py`](assignment-2/spatial_join.py)
![spatial_join.png](assignment-2/spatial_join.png)

---

## Assignment 3: Rasterio

Aim for 2–4 sentences per answer. Your code goes in `assignment-3/landsat.py`.

**Q1 — rasterio profile type:** After opening a Landsat raster with `rasterio.open()` and printing `src.profile`, what Python `type` is `src.profile`?

_Your answer here._

**Q2 — profile key-value pairs:** List the key-value pairs in `src.profile` and explain what each one means. What does `crs` tell you? What does `transform` describe? What do `width` and `height` represent?

_Your answer here._

**Q3 — masking NoData values:** Explain what `thumbnail[thumbnail == 0] = np.nan` does and why it is necessary.

_Your answer here._

**Q4 — Cloud Optimized GeoTIFF (COG):** What is a COG and why would you use one instead of a regular GeoTIFF when working with large files in cloud storage like AWS S3?

_Your answer here._

**Q5 — Decimation:** What is decimation in the context of raster data? How does rasterio use it to efficiently read overview (reduced-resolution) versions of large rasters?

_Your answer here._

**Q6 — Calculate mNDWI (independent task):** Write a function `calc_mndwi()` that calculates the Modified Normalized Difference Water Index, `mNDWI = (Green - SWIR) / (Green + SWIR)`. For Landsat 8, Green = Band 3 and SWIR = Band 6. Add it to `assignment-3/landsat.py`, call it, plot the result, and paste the function here.

_Your answer here._

```python
def calc_mndwi():
    pass  # replace with your implementation
```

**Q7 — pyproj:** What is `pyproj` used for? Have you used another library in this course that can do coordinate transformations? Name it and compare.

_Your answer here._

**Q8 — Image vs. real-world coordinates:** How can you use rasterio to translate between pixel coordinates (row, column) and geographic coordinates (latitude/longitude)? Name the rasterio method and explain how it works.

_Your answer here._

**Q9 — Custom NDVI difference visualization (independent task):** Modify the NDVI difference plot from the tutorial into a single standalone plot (not a subplot) using a colormap not used anywhere in the tutorial, with a colorbar legend. Include the code in `landsat.py`. What colormap did you choose and why?

_Your answer here._

**Q10 — Reprojection:** Reproject the Landsat scene to California State Plane Zone 3 (EPSG:2227) and include the code in `landsat.py`. What changes when you reproject: does the pixel count change? Does the transform change?

_Your answer here._

**Files for this assignment** (add them to `assignment-3/`):

- [`assignment-3/landsat.py`](assignment-3/landsat.py)
![screencap_mndwi.png](assignment-3/screencap_mndwi.png)

![screencap_ndvi_difference.png](assignment-3/screencap_ndvi_difference.png)

---

## Assignment 4: Spatial Python with Jupyter Notebooks

**Files for this assignment** (add them to `assignment-4/`):

- [`assignment-4/wards-barricades.ipynb`](assignment-4/wards-barricades.ipynb)
![screencap-hello.png](assignment-4/screencap-hello.png)

![screencap-california-housing.png](assignment-4/screencap-california-housing.png)

![screencap-streetlights.png](assignment-4/screencap-streetlights.png)

![screencap-wards.png](assignment-4/screencap-wards.png)
