# Data Folder

This folder contains sample datasets used by the provided notebooks.

## Files Included

| File | Used By | Description |
|---|---|---|
| `Tucson_Streetlights.geojson` | `streetlights-assignment.ipynb` | City of Tucson streetlight point locations |
| `Tucson_Council_Districts.geojson` | `streetlights-assignment.ipynb` | Tucson city council district polygons |

## Where to Download Data

### Tucson Streetlights
1. Go to [gisdata.tucsonaz.gov](https://gisdata.tucsonaz.gov)
2. Search for "streetlights"
3. Download as GeoJSON or Shapefile
4. Place in this `data/` folder

### Tucson Council Districts
1. Go to [gisdata.tucsonaz.gov](https://gisdata.tucsonaz.gov)
2. Search for "council districts"
3. Download as GeoJSON or Shapefile
4. Place in this `data/` folder

## Notes

- The notebooks read from this folder using relative paths — do not move files outside `data/`
- If you download shapefiles instead of GeoJSON, update the file paths in the notebook
- Make sure both layers use the same CRS before running `sjoin`. Check with `.crs` and reproject if needed: `streetlights = streetlights.to_crs(districts.crs)`
