import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid_data.csv")
df = df.drop(columns=["Unnamed: 0","Admin2","FIPS","OBJECTID","Combined_Key"])
df.columns = ['State', 'Country', 'LastUpdate', 'Lat', 'Long','Confirmed', 'Recovered', 'Deaths', 'Active']
print(df)
#print(df.isnull().sum())