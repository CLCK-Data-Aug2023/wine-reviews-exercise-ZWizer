# add your code here

import pandas as pd 

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

country_summary = df.groupby('country').agg({'points': ['count', 'mean']}).reset_index()
country_summary.columns = ['Country', 'Number of Reviews', 'Average Points']
country_summary['Average Points'] = country_summary['Average Points'].round(1)
country_summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data has been written to reviews-per-country.csv file")
