import pandas as pd

df = pd.read_csv("total_stars.csv")
print(df)

df.columns

df = df.drop(['Luminosity','id.1', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Unnamed: 6'], axis=1)

df.describe()
df.info()
df.dtypes

df.to_csv('final_data.csv', index=True)
