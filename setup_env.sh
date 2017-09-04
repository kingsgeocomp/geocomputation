#!/usr/bin/bash

ENVNM="gsa2017"

printf "Updating conda...\n"
conda update --quiet --yes conda

# If already exists:
# conda env remove -n gsa2017

printf "Creating environment\n"
conda create -n "$ENVNM" -y -f python=2.7 anaconda

printf "Activating environment\n"
source activate "$ENVNM"

printf "Insalling required notebook packages\n"
conda install -y ipython jupyter nb_conda

printf "Installing default packages\n"
conda install -y matplotlib numpy scipy seaborn=0.8* scikit-learn=0.18* statsmodels=0.8.0 basemap requests 

printf "Installing packages from conda-forge...\n"
conda install --y -c conda-forge clusterpy=0.9.9 geopandas=0.2* palettable=3.* pysal=1.13* folium mplleaflet rasterio fiona

# From Source
printf "Installing final packages via pip...\n"
pip install cenpy
pip install sompy

printf "Exporting to YAML for cloning...\n"
conda env export > "$ENVNM.yml

printf "Done.\n"
source deactivate "$ENVNM"
