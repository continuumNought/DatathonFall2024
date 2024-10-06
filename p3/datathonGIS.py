import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
# Load CSV data
df = pd.read_csv(/home/michael/Downloads/JNorthMonarch.csv)
geometry = [Point(xy) for xy in zip(df.longitude, df.latitude)]
gdf = gpd.GeoDataFrame(df, geometry=geometry)/
