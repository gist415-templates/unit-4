# Assignment 3: Rasterio — Questions

Answer each question below. Aim for 2–4 sentences per answer. Add your answers directly in this file beneath each question heading.

---

## Q1 — rasterio profile type

After opening a Landsat raster with `rasterio.open()` and printing `src.profile`, what Python `type` is `src.profile`?

**Answer:**

---

## Q2 — profile key-value pairs

List the key-value pairs in `src.profile` and explain what each one means. What does `crs` tell you? What does `transform` describe? What do `width` and `height` represent?

**Answer:**

---

## Q3 — masking NoData values

Explain what `thumbnail[thumbnail == 0] = np.nan` does and why it is necessary.

**Answer:**

---

## Q4 — Cloud Optimized GeoTIFF (COG)

What is a COG and why would you use one instead of a regular GeoTIFF when working with large files in cloud storage like AWS S3?

**Answer:**

---

## Q5 — Decimation

What is decimation in the context of raster data? How does rasterio use it to efficiently read overview (reduced-resolution) versions of large rasters?

**Answer:**

---

## Q6 — Calculate mNDWI (Independent Task)

The tutorial walks through NDVI = (NIR - Red) / (NIR + Red) using Landsat 8 Bands 5 and 4.

Write a function `calc_mndwi()` that calculates the Modified Normalized Difference Water Index:
`mNDWI = (Green - SWIR) / (Green + SWIR)`

For Landsat 8: Green = Band 3, SWIR = Band 6. Add this function to `assignment-3/landsat.py`, call it, and plot the result.

**Paste your function here:**

```python
def calc_mndwi():
    pass  # replace with your implementation
```

---

## Q7 — pyproj

What is `pyproj` used for? Have you used another library in this course that can do coordinate transformations? Name it and compare.

**Answer:**

---

## Q8 — Image coordinates vs. real-world coordinates

How can you use rasterio to translate between pixel coordinates (row, column) and geographic coordinates (latitude/longitude)? Name the rasterio method and explain how it works.

**Answer:**

---

## Q9 — Custom NDVI difference visualization (Independent Task)

Modify the NDVI difference plot from the tutorial to produce a single standalone plot (not a subplot) using a colormap NOT used anywhere in the tutorial. Add a colorbar legend.

What colormap did you choose and why?

**Answer:**

---

## Q10 — Reprojection

Reproject the Landsat scene to **California State Plane Zone 3 (EPSG:2227)**. Include the reprojection code in `landsat.py`.

Describe what changes when you reproject: does the pixel count change? Does the transform change?

**Answer:**
