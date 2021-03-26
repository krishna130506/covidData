import plotly.express as px
import pandas as pd

df = pd.read_csv("covidData.csv")
fig = px.scatter(df,x = "date", y = "cases",color = "country")
fig.show()