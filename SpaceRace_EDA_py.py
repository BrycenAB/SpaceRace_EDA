import pandas as pd
import plotly.express as px

df = pd.read_csv('Space_Corrected.csv')
df.head()

# remove unnecessary columns
df = df.drop(columns=['Unnamed: 0'])
df = df.drop(columns=['Unnamed: 0.1'])
df.head()

df.info()

df.isnull().sum()

print('Total number of launches: ' + str(df['Company Name'].count()))

# number of launches per company
df['Company Name'].value_counts()

df['Status Mission'].value_counts()

df['Location'].value_counts()

# data cleaning -------------
from datetime import datetime, timezone

# Convert 'datum' column to datetime
df['Datum'] = pd.to_datetime(df['Datum'], format='%a %b %d, %Y %H:%M %Z', errors='coerce')
df.head(50)

# create a new column with the year of the launch
df['Year'] = df['Datum'].dt.year

# create a new column with the month of the launch
df['Month'] = df['Datum'].dt.month

df.head()


# data visualization -----------
# How did the rate of launches change over the years? ----------

# create a new dataframe with the number of launches by year
df_year = df['Year'].value_counts().reset_index()

rename = {
    'index': 'Year',
    'Year': 'Count'
}

df_year = df_year.rename(columns=rename)

# graph with year being the color
fig = px.bar(df_year, x='Year', y='Count', color='Year', title='Number of launches by year' , )
fig.show()

# create a new dataframe with the number of launches by location
df_loc = df['Location'].value_counts().reset_index()

# rename Location element to last string in the location string
df_loc['index'] = df_loc['index'].str.split(',').str[-1]

# get total number of launches by location
total = df_loc['Location'].sum()

# How many launches per location ? ----------

# create a new dataframe containing unique locations and the number of launches
df_loc = df_loc.groupby('index').sum().reset_index()

# add column with count of launches by location
df_loc['count'] = df_loc['Location']

# sort dataframe by number of launches
df_loc = df_loc.sort_values(by='count', ascending=False)

# graph with location being the color
fig = px.bar(df_loc, x='index', y='count', color='index', title='Number of launches by location')
fig.show()

# How many launches per company ? ----------

# create a new dataframe with the number of launches by company
df_company = df['Company Name'].value_counts().reset_index()

# get total number of launches by company
total = df_company['Company Name'].sum()

# create a new dataframe containing unique companies and the number of launches
df_company = df_company.groupby('index').sum().reset_index()

rename = {
    'index': 'Company Name',
    'Company Name': 'count'
}

df_company = df_company.rename(columns=rename)

# sort dataframe by number of launches
df_company = df_company.sort_values(by='count', ascending=False)

# reduce dataframe to top 20 companies
df_company = df_company.head(20)

# graph with company being the color
fig = px.bar(df_company, x='Company Name', y='count', color='Company Name', title='Top 20 Number of launches by company')
fig.show()

# What is the success rate of all launches? ----------

# create a new dataframe with the number of launches by status
df_status = df['Status Mission'].value_counts().reset_index()

# get total number of launches by status
total = df_status['Status Mission'].sum()

# create a new dataframe containing unique status and the number of launches
df_status = df_status.groupby('index').sum().reset_index()

rename = {
    'index': 'Status Mission',
    'Status Mission': 'count'
}

df_status = df_status.rename(columns=rename)

# sort dataframe by number of launches
df_status = df_status.sort_values(by='count', ascending=False)

# convert total launches to a percentage
df_status['percentage'] = df_status['count'] / total * 100

# pie chart displaying the percentage of launches by status
fig = px.pie(df_status, values='percentage', names='Status Mission', title='Percentage of launches by status')
fig.show()


# What is the success rate of the launches per year? ----------

# create a new dataframe with the number of launches by year and status
df_year_status = df.groupby(['Year', 'Status Mission']).size().reset_index()

rename = {
    0: 'count'
}

df_year_status = df_year_status.rename(columns=rename)

# graph with year being the color
fig = px.bar(df_year_status, x='Year', y='count', color='Status Mission', title='Number of launches by year and status', facet_row_spacing=0.1)
fig.show()

# How has the cost of launches changed over time ? ----------

import statsmodels.api as sm
# create a new dataframe with the year and cost of each launch
df_cost = df[['Year', ' Launch Cost']].dropna()

# convert cost to a float
df_cost[' Launch Cost'] = df_cost[' Launch Cost'].str.replace(',', '').astype(float)

# convert from "##.#" to millions
df_cost[' Launch Cost'] = df_cost[' Launch Cost'] * 1000000

# remove outliers
df_cost = df_cost[df_cost[' Launch Cost'] < 400000000]

# graph with year being the color
fig = px.scatter(df_cost, x='Year', y=' Launch Cost', color=' Launch Cost', title='Cost of launches by year', trendline='ols')
fig.show()

# create a new dataframe with the average cost of launches by year
df_cost_year = df_cost.groupby('Year').mean().reset_index()

# graph with year being the color
fig = px.bar(df_cost_year, x='Year', y=' Launch Cost', color=' Launch Cost', title='Average cost of launches by year')
fig.show()

# How has the cost of launches changed over time per company ? ----------

import plotly.graph_objs as go
# create a new dataframe with the year, company and cost of each launch
df_cost_company = df[['Year', 'Company Name', ' Launch Cost']].dropna()

# remove 0 cost launches
df_cost_company = df_cost_company[df_cost_company[' Launch Cost'] != 0]

# convert cost to a float
df_cost_company[' Launch Cost'] = df_cost_company[' Launch Cost'].str.replace(',', '').astype(float)

# convert from "##.#" to millions
df_cost_company[' Launch Cost'] = df_cost_company[' Launch Cost'] * 1000000

# remove outliers
df_cost_company = df_cost_company[df_cost_company[' Launch Cost'] < 400000000]

# Fit the regression model
X = df_cost_company['Year']
y = df_cost_company[' Launch Cost']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

# Get the predicted values
predictions = model.predict(X)

# Add the trendline to the scatter plot
fig = px.scatter(df_cost_company, x='Year', y=' Launch Cost', color='Company Name', title='Cost of launches by year and company', trendline='ols')
fig.add_traces(go.Scatter(x=df_cost_company['Year'], y=predictions, mode='lines', name='overall Trend-line'))
fig.show()


