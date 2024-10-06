import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

def main():
    counties = pd.read_csv('County_Pesticide.csv')
    counties.FIPS = counties.FIPS.astype(str)

    for year in [2002,2012,2017]:
        county_shapes = gpd.read_file('./shapefiles/US_counties_2012_geoid.shp')
        county_shapes['Probability'] = 0.0

        county_shapes_year = gpd.GeoDataFrame(county_shapes)
        for index, row in counties[counties['Year'] == year].iterrows():
            if row['FIPS'] in county_shapes_year['FIPS'].values:
                county_shapes_year.at[index, 'Probability'] = row['Probability']

        fig, ax = plt.subplots(1, 1)
        county_shapes_year.plot(
            column='Probability',
            ax=ax,
            legend=True,
        )
        plt.title(f"Pesticide Use by County {year}")
        plt.savefig(f"Pesticide_Map_{year}.jpeg",format="jpeg")
        plt.clf()


main()
