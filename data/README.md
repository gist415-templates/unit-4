# Data Folder

Put the data for Assignments 3 and 4 in this folder. The data files are not included in the repository: download them as described below. The Docker container can only see files inside this repository, so a copy left in your Downloads folder cannot be opened from Python.

| File | Used By | Where it comes from |
|---|---|---|
| `landsat/` (six `.TIF` files) | Assignment 3, `assignment-3/landsat.py` | `gist415-landsat.zip` in D2L |
| `Tucson_Streetlights.geojson` | Assignment 4, `streetlights-assignment.ipynb` | City of Tucson open data |
| `Tucson_Council_Districts.geojson` | Assignment 4, `streetlights-assignment.ipynb` | City of Tucson open data |

## Landsat 8 (Assignment 3)

1. Download `gist415-landsat.zip` from the D2L Unit 4 content area
2. Unzip it into this `data/` folder, so the files are at `data/landsat/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF` and so on

These are the two Landsat 8 scenes from the rasterio tutorial (16 June 2017 and 19 June 2018), bands 3, 4, 5 and 6, at 90 m pixels with built-in overviews. In Python, open them as `/home/jovyan/work/data/landsat/<file name>`.

`data/landsat/` is listed in `.gitignore`, so GitHub Desktop does not offer to commit it. Do not commit the data.

## Tucson Streetlights (Assignment 4)

1. Go to [gisdata.tucsonaz.gov](https://gisdata.tucsonaz.gov)
2. Search for "streetlights" and open **Streetlights - City of Tucson - Open Data**
3. Download it as GeoJSON
4. Save it in this `data/` folder as `Tucson_Streetlights.geojson`

## Tucson Council Districts (Assignment 4)

Tucson's council districts are its six wards.

1. Go to [gisdata.tucsonaz.gov](https://gisdata.tucsonaz.gov)
2. Search for "ward boundaries" and open **City of Tucson Ward Boundaries** (not the one marked Deprecated)
3. Download it as GeoJSON
4. Save it in this `data/` folder as `Tucson_Council_Districts.geojson`

## Notes

- The notebooks read from this folder using relative paths — do not move files outside `data/`
- If you download shapefiles instead of GeoJSON, update the file paths in the notebook
- Make sure both layers use the same CRS before running `sjoin`. Check with `.crs` and reproject if needed: `streetlights = streetlights.to_crs(districts.crs)`
