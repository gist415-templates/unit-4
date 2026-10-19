# GIST 415 Python environment: JupyterLab plus the geospatial libraries used in Units 3, 4 and 7.
#
# Build once (from the folder that contains the environment/ folder):
#   docker build -t gist415-python ./environment
#
# Run (from your unit repository folder):
#   docker run --rm -it -p 8888:8888 -v "${PWD}:/home/jovyan/work" gist415-python

# Official Jupyter Docker Stacks image: Python, JupyterLab, pandas, NumPy, matplotlib.
# A dated tag never changes, so everyone builds on the same base.
FROM quay.io/jupyter/scipy-notebook:2026-10-05

# Geospatial libraries from conda-forge, which builds GDAL, GEOS and PROJ to work together.
RUN mamba install --yes --channel conda-forge \
        "geopandas=1" \
        "rasterio=1" \
        rasterstats \
        geodatasets \
        mapclassify \
    && mamba clean --all --force-pkgs-dirs --yes \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"
