# Import libraries
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import plotly

# Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:
# Use datetime to set start and end datetime objects.
start = dt.datetime(2006, 1, 1)
end = dt.datetime(2016, 1, 1)
# Figure out how to use datareader to grab info on the stock.
df = pd.read_pickle("all_banks")
print(df.info())
print(df)

# What is the max Close price for each bank's stock throughout the time period?
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
for tick in tickers:
    print(tick, ': ', str(df[tick]['Close'].max()))

# Alternative approaches
print(df.xs(key='Close', axis=1, level='Stock Info').max())
print(df.xs(key='Close', axis=1, level=1).max())

# Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:
returns = pd.DataFrame()

# We can use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.*
for tick in tickers:
    returns[tick+" Return"] = df[tick]['Close'].pct_change()
print(returns.info())
print(returns.head())

# Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?
# sns.pairplot(returns[1:])
# plt.show()

# Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?
best_day = {}
worst_day = {}
for tick in tickers:
    date = str(returns[returns[tick+' Return'] == returns[tick+' Return'].max()].index[0].date())
    pct_change = float(returns[tick+' Return'].max())
    best_day[tick] = [date, pct_change]

    date = str(returns[returns[tick+' Return'] == returns[tick+' Return'].min()].index[0].date())
    pct_change = float(returns[tick+' Return'].min())
    worst_day[tick] = [date, pct_change]

print(best_day)
print(worst_day)

# Alternative approach
print(returns.idxmax())
print(returns.idxmin())

# Take a look at the standard deviation of the returns, which stock would you classify as the riskiest over the entire time period? Which would you classify as the riskiest for the year 2015?
print(returns.std())
print(returns[returns.index >= dt.datetime(2015, 1, 1)].std())

# Alternative
print(returns.loc['2015-01-01':'2015-12-31'].std())

# Create a distplot using seaborn of the 2015 returns for Morgan Stanley
# sns.distplot(returns.loc['2015-01-01':'2015-12-31', 'MS Return'])
# plt.show()

# Create a distplot using seaborn of the 2008 returns for CitiGroup
# sns.distplot(returns.loc['2008-01-01':'2008-12-31', 'C Return'])
# plt.show()

# More visualisation
# Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use .xs to get a cross section of the data.)
close = pd.DataFrame()
for tick in tickers:
    close[tick+' Close'] = df.xs(key=(tick, 'Close'), axis=1, level=('Bank Ticker', 'Stock Info'))
# close.plot.line()
# plt.show()

# Alternative
# df.xs(key='Close', axis=1, level='Stock Info').plot()
# plt.show()

# Moving averages
# Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
bac_return = pd.DataFrame()
bac_return['BAC Close'] = df.xs(key=('BAC', 'Close'), axis=1, level=('Bank Ticker', 'Stock Info'))['2008-01-01':'2009-01-01']
bac_return['MA'] = bac_return['BAC Close'].rolling(window=30).mean()
bac_return.plot.line()
plt.show()
# Alternative
plt.figure(figsize=(12, 6))
df['BAC']['Close']['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Moving Average')
df['BAC']['Close']['2008-01-01':'2009-01-01'].plot(label='BAC Closing Price')
plt.show()

# Create a heatmap of the correlation between the stocks Close Price.
sns.heatmap(data=df.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
plt.show()