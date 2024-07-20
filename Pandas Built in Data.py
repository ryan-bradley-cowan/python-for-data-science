# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df3 = pd.read_csv('df3.txt')

# Show head and info
print(df3.head())
print(df3.info())

# Scatter plot
df3.plot.scatter(x='a', y='b')
plt.show()

# Histogram
df3['a'].plot.hist(bins=10)
plt.show()

# Box plot
df3[['a', 'b']].plot.box()
plt.show()

# kde plot
df3['d'].plot.kde()
plt.show()

# area plot
df3.iloc[0:30, :].plot.area()
plt.show()