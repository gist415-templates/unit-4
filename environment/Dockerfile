# GIST 415 Python environment: JupyterLab plus the geospatial libraries used in Units 3, 4 and 7.
#
# Students normally do not build this directly. From the folder that holds compose.yaml:
#   docker compose up        (builds on first use, then starts JupyterLab)
#   docker compose down      (stops it)
#
# Quick test:
#   docker compose run --rm jupyter check-environment

# Official Jupyter Docker Stacks image: Python 3.13 and JupyterLab.
# A dated tag never changes, so every build starts from the same base.
FROM quay.io/jupyter/minimal-notebook:2026-10-05

# Every library at the exact version listed in environment.yml, from conda-forge,
# which builds GDAL, GEOS and PROJ to work together.
COPY --chown=${NB_UID}:${NB_GID} environment.yml /tmp/environment.yml
RUN mamba env update --name base --file /tmp/environment.yml \
    && mamba clean --all --force-pkgs-dirs --yes \
    && rm /tmp/environment.yml \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

# Cache the GeoPandas tutorial's sample data (NYC boroughs) so Unit 4 Assignment 1
# works without depending on the download site. Not fatal if the site is down.
RUN python -c "import geodatasets; geodatasets.get_path('nybb')" \
    || echo "WARNING: could not cache the nybb sample data; it will download on first use"

# The quick test, available as a command inside the container.
COPY --chmod=0755 check_environment.py /usr/local/bin/check-environment
