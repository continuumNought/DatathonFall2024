# DatathonFall2024

## Problem Reproduction
Before running these examples start a fresh virtual environment and load requirements.txt.

### Problem 1
Put the files `AgCensus_MasterDataFrame.txt`,`USDA_PDP_AnalyticalResults.csv` in the
working directory where you want to run the scripts under p1.
Call the scripts in the p1 folder in the following order
1. `get_ag_data.py`
2. `get_pdp_data.py`
3. `join_ag_pdp.py`
4. `make_graph_data.py`
5. `county_maps.py`
After all scripts have been successfully run you'll have a bunch of artifacts in your
working directory.
The jpeg files are the graphs for the years indicated in their titles.
The data used to generate these graphs is in `County_Pesticide.csv`.
