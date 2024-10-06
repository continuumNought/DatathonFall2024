import numpy as np
import pandas as pd

pdp = pd.read_csv("pdp_data.csv")
bflies = pd.read_csv("butterflies_data.csv")
cncavgs = {}
pesticides = set()

pdp = pdp[pdp['concentration'].notna()]
for i in pdp["pesticide_name"]:
    pesticides.add(i)

for s in pesticides:
    # Create a boolean mask where 'StringColumn' contains the string s
    mask = pdp['pesticide_name'].str.contains(s, case=False, na=False)
    
    # Filter the DataFrame
    filtered_df = pdp[mask]
    
    # Compute the average of 'FloatColumn'
    if not filtered_df.empty:
        average = filtered_df['concentration'].mean()
    else:
        average = None  # Or you can set to 0 or np.nan if preferred
    
    # Store the result in the dictionary
    cncavgs[s] = average

result_df = pd.DataFrame({'String': list(cncavgs.keys()), 'Average': list(cncavgs.values())})
print(result_df)

