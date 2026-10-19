# GIST 415 — Unit 4: Python Geospatial

This is your **Unit 4 repository**. You create it once, in Assignment 1, and use it for all 4 Unit 4 assignments. Do not create another repository for this unit.

Written answers go in [`SUBMISSION.md`](SUBMISSION.md). Screenshots and other files go in each assignment's `assignment-N/` folder.

## Setting Up This Repository (Assignment 1)

1. On the template page, click **Use this template** → **Create a new repository**
2. Set **Owner** to the class GitHub organization (the name is in the D2L course announcement), not your personal account
3. Name it exactly `gist415-unit-4-YOUR_NETID` (for example `gist415-unit-4-jsmith`)
4. Set visibility to **Private**
5. Click **Create repository**, then clone it with GitHub Desktop (**File → Clone Repository**)
6. In GitHub Desktop, create a branch named `unit-4-work` (**Current Branch → New Branch**) and click **Publish branch**

## Assignments

| Assignment | What you submit | Points |
|---|---|---|
| A1: GeoPandas Introduction | `assignment-1/screencap-workspace-gdf.png`, `assignment-1/screencap-gdf-dist.png`, `assignment-1/screencap-gdf-centroids.png`, `assignment-1/screencap-gdf-buffered-centroid.png` | 25 |
| A2: GeoPandas Spatial Join | `assignment-2/spatial_join.py`, `assignment-2/spatial_join.png` | 25 |
| A3: Rasterio | `SUBMISSION.md` section, `assignment-3/landsat.py`, `assignment-3/screencap_mndwi.png`, `assignment-3/screencap_ndvi_difference.png` | 25 |
| A4: Spatial Python with Jupyter Notebooks | `assignment-4/wards-barricades.ipynb`, `assignment-4/screencap-hello.png`, `assignment-4/screencap-california-housing.png`, `assignment-4/screencap-streetlights.png`, `assignment-4/screencap-wards.png` | 25 |
| **Unit 4 total** | | **100** |

Full instructions for each assignment are in D2L.

## How to Submit

You work on **one branch** and open **one Pull Request** for the whole unit.

1. Commit all Unit 4 work to your `unit-4-work` branch
2. In Assignment 1, open a Pull Request from `unit-4-work` → `main`, titled `Unit 4 Submission — YOUR_NETID`
3. For each later assignment, commit and push to the same branch; the same Pull Request updates automatically
4. After Assignment 4, check that every row of the checker's comment shows ✅, then submit the Pull Request URL in the D2L Unit 4 submission folder

**Do not merge the Pull Request.** Leave it open for instructor review.

## Provided Notebooks (run these as part of assignments)

| File | Used In | Purpose |
|---|---|---|
| `hello.ipynb` | Assignment 4 | Basic Python & Jupyter intro |
| `California Housing.ipynb` | Assignment 4 | Choropleth from census housing data |
| `airports.ipynb` | Assignment 4 | Airport point mapping (reference only) |
| `streetlights-assignment.ipynb` | Assignment 4 | Spatial join — Tucson streetlights × council districts |
| `data/` | Assignment 4 | Sample datasets for the provided notebooks |

## Starting the Docker Python Environment

The `environment/` folder holds the Dockerfile for the course Python image: JupyterLab plus GeoPandas, Rasterio and the other libraries this course uses. You do not need Anaconda or Python installed on your computer.

If you built the image in Unit 3 on this computer, skip this step. Otherwise build it once, in PowerShell (Windows) or Terminal (Mac), from this repository's folder:

```
docker build -t gist415-python ./environment
```

Then, from this repository's folder, start JupyterLab each work session:

```
docker run --rm -it -p 8888:8888 -v "${PWD}:/home/jovyan/work" gist415-python
```

Open the URL the terminal prints, double-click `work` in the file browser, and save everything inside `work`. Full instructions: **Reference: Python Docker Environment for Units 3-4** in D2L, and Lecture 3.1.

## Automated Checker

When you open or update your Pull Request, a GitHub Action posts a comment listing, for each assignment, whether its `SUBMISSION.md` section is answered and its required files are present. Assignments you have not reached yet show ❌ until you complete them.
