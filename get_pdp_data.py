import pandas as pd


FIELDS = [
    'Pesticide Code',
    'Pesticide Name',
    'Test Class',
    'Concentration',
    'LOD',
    'pp_',
    'Confirm 1',
    'Confirm 2',
    'Annotate',
    'Quantitate',
    'Mean',
    'Extract',
    'Determ',
    'EPA Tolerance (ppm)',
]


COMM_DICT = {
    "BY": "Brl",
    "CB": "Crn",
    "CD": "Crn",
    "CO": "Crn",
    "CS": "Crn",
    "CY": "Crn",
    "OA": "Oat",
    "PB": "Pnt",
    "IS": "Ptt",
    "PO": "Ptt",
    "PZ": "Ptt",
    "RI": "Ric",
    "SY": "Soy",
    "YF": "Soy",
    "SW": "Swt",
    "WF": "Wht",
    "WH": "Wht",
    "BA": "Cat",
    "BL": "Cat",
    "BM": "Cat",
    "KA": "Swn",
    "KM": "Swn",
}


def tokenize_sample_id(sample_id):
    state = sample_id[0:2]
    year = int(sample_id[2:4])
    month = int(sample_id[4:6])
    day = int(sample_id[6:8])

    if year > 90:
        year += 1900

    else:
        year += 2000

    return (state,year,month,day)


def get_remaining_columns(row):
    return [row[f] for f in FIELDS]


def data_gen(df):
    for _,row in df.iterrows():
        commodity = row['Commod']
        if commodity in COMM_DICT:
            yield (
                *tokenize_sample_id(row['Sample ID']),
                COMM_DICT[commodity],
                *get_remaining_columns(row)
            )


def main():
    df = pd.read_csv('USDA_PDP_AnalyticalResults.csv', low_memory=False)
    ndf = pd.DataFrame(data_gen(df), columns=['State','Year','Month','Day','Commod',*FIELDS])
    ndf.to_csv('PDP_Data.csv',index=False)


main()
