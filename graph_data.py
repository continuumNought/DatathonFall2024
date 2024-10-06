import pandas as pd


def gen_county(df,state,year):
    pest_commod = df[['Pesticide Code','Commodity']].drop_duplicates()
    m = len(pest_commod)
    n = len(df['FIPS'].unique())
    for county in df['FIPS'].unique():
        county_data = df[df['FIPS'] == county]
        pc_pairs = county_data[['Pesticide Code','Commodity']].drop_duplicates()
        k = len(pc_pairs)
        p = k/(m*n)
        yield (state,year,county,p)



def main():
    df = pd.read_csv('Ag_PDP_join.csv',low_memory=False)

    # For each year, for each state there are commodities and pesticides
    # In each county there are commodities and pesticides.
    # Let R be the relation between pesticides P and commodities C in State
    # S at year Y. Moreover m = size(R). If there are
    # n counties and county K has k pesticide commodity pairs then the chance
    # of K having any pesticide is k/(mn).
    columns = ['STATE','Year','FIPS','Probability']
    ndf = pd.DataFrame(None,columns=columns)
    for year in sorted(df['Year'].unique()):
        for state in sorted(df['STATE'].unique()):
            df_year = df[df['Year'] == year]
            df_state_year = df_year[df_year['STATE'] == state]
            county_data = pd.DataFrame(
                gen_county(df_state_year,state,year),
                columns=columns
            )
            ndf = pd.concat([ndf,county_data],ignore_index=True)

    ndf.to_csv('County_Pesticide.csv',index=False)


main()
