import plotly
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("covid_data.csv")
df = df.drop(columns=["Unnamed: 0","Admin2","FIPS","OBJECTID","Combined_Key"])
df.columns = ['State', 'Country', 'LastUpdate', 'Lat', 'Long','Confirmed', 'Recovered', 'Deaths', 'Active']
#print(df)

df["State"] = df["State"].fillna(value="")
deaths = df.groupby("Country")["Deaths"].sum().nlargest(10)
deaths = pd.DataFrame(deaths)

bar = px.bar(deaths,x=deaths.index,y="Deaths",color=deaths.index,color_discrete_sequence=px.colors.qualitative.Set3,title="Top countries for COVID-19 deaths")
bar.show()

# figure = px.scatter(deaths,x=deaths.index,y="Deaths",color=deaths.index,size="Deaths")
# figure.show()

states = df[df["Country"] == "US"]
figure = go.Figure(data=[
    go.Bar(name="Confirmed Cases",x=states["Confirmed"],y=states["State"],orientation="h"),
    go.Bar(name="Deaths",x=states["Deaths"],y=states["State"],orientation="h")
])
figure.update_layout(height=600)
figure.show()

# cases = states.nlargest(10,"Confirmed")
# s_deaths = states.nlargest(10,"Deaths")

# scatter = px.scatter(cases,x="Confirmed",y="Deaths",hover_name="State",title="Cases and deaths for top US states")
# scatter.write_html("scatter.html")