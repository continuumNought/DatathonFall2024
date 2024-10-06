import pandas as pd


def main():
    df_ag = pd.read_csv('Ag_Data.csv')

    df_pdp = pd.read_csv('PDP_Data.csv')
    df_pdp = df_pdp.rename(columns={
        'Commod':'Commodity',
        'State':'STATE',
        'Month':'Month_PDP',
        'Day':'Day_PDP',
    })

    df_joined = pd.merge(
        df_ag,
        df_pdp,
        how='left',
        on=['STATE','Year','Commodity'],
        suffixes=['_AG','_PDP'],
    )
    # No Concentration values are null so if they show up as
    # null in the join then the ag row failed to match a pdp row
    # so we can get rid of it
    df_joined = df_joined[df_joined['Concentration'].notna()]

    df_joined.to_csv('Ag_PDP_join.csv',index=False)


main()
