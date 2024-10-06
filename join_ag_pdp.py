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

    df_joined.to_csv('Ag_PDP_join.csv',index=False)


main()
