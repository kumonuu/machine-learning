import plotly
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("covid_data.csv")
df = df.drop(columns=["Unnamed: 0","Admin2","FIPS","OBJECTID","Combined_Key"])
df.columns = ['State', 'Country', 'LastUpdate', 'Lat', 'Long','Confirmed', 'Recovered', 'Deaths', 'Active']
#print(df)

df["State"] = df["State"].fillna(value="")
deaths = df.groupby("Country")["Deaths"].sum().nlargest(10)
deaths = pd.DataFrame(deaths)

figure = px.scatter(deaths,x=deaths.index,y="Deaths")
figure.show()