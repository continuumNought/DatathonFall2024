import pandas as pd
import geopandas as gpd


def main():
    shapefile_path = './shapefiles/US_counties_2012_geoid.shp'
    polygons = gpd.read_file(shapefile_path)
    polygons_pandas = pd.DataFrame(polygons)
    polygons_pandas['FIPS'] = polygons_pandas['FIPS'].astype(int)
    polygons_pandas.dtypes

    ag_data_path = './AgCensus_MasterDataFrame.txt'
    ag_data = pd.read_csv(ag_data_path, sep='\t')

    counties = pd.merge(polygons_pandas, ag_data, left_on='FIPS', right_on='FIPS', how='left')
    commodity_columns = list(counties.columns)
    columns_to_remove = ['FIPS', 'geometry', 'STATE', 'COUNTY', 'STCTY', 'AREA_KM', 'Bailey_Eco', 'USDA_FRR', 'Lon', 'Lat']
    for column in columns_to_remove:
        commodity_columns.remove(column)

    fields = [
        'FIPS',
        'geometry',
        'STATE',
        'COUNTY',
        'STCTY',
        'AREA_KM',
        'Bailey_Eco',
        'USDA_FRR',
        'Lon',
        'Lat',
        'Commodity',
        'Year',
        'Quantity',
    ]

    def new_data_it():
        for _, row in counties.iterrows():
            for column in commodity_columns:
                year = int(column[3:])
                if year >= 1990:
                    new_row = [
                        row['FIPS'],
                        row['geometry'],
                        row['STATE'],
                        row['COUNTY'],
                        row['STCTY'],
                        row['AREA_KM'],
                        row['Bailey_Eco'],
                        row['USDA_FRR'],
                        row['Lon'],
                        row['Lat']
                    ]
                    new_row.append(column[:3])
                    new_row.append(year)
                    new_row.append(row[column])
                    yield new_row

    new_counties = pd.DataFrame(new_data_it(), columns=fields)
    new_counties.to_csv('Ag_Data.csv',index=False)


main()
