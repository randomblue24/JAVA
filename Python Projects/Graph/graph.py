import pandas as pd
import plotly.express as px


df = pd.read_csv(r"C:\Users\Node 1\Downloads\Water_Consumption_In_The_New_York_City.csv")
fig = px.line(df, x = 'Year', y = 'NYC Consumption(Million gallons per day)', title='NYC Consumption of Water (millions of gallons/day)')
fig.show()

fig2 = px.line(df, x = 'New York City Population', y = 'NYC Consumption(Million gallons per day)', title='NYC Consumption of Water (millions of gallons/day)')
fig2.show()