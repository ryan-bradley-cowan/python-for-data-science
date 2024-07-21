# Import Import numpy and pandas libraries
import numpy as np
import pandas as pd


# Import visualization libraries and set %matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

#  Read in the csv file as a dataframe called df
df = pd.read_csv('911.csv')

# Check the info() of the df
print(df.info())

# Check the head of df
print(df.head())

# What are the top 5 zipcodes for 911 calls?
print(df['zip'].value_counts().head(5))

# What are the top 5 townships (twp) for 911 calls?
print(df['twp'].value_counts().head(5))

# Take a look at the 'title' column, how many unique title codes are there?
print(df['title'].nunique())

# In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
print(df['Reason'][:5])

# What is the most common Reason for a 911 call based off of this new column?
print(df['Reason'].value_counts())

# Now use seaborn to create a countplot of 911 calls by Reason.
sns.countplot(data=df, x='Reason')
plt.show()

# Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
print(type(df['timeStamp'][0]))

# You should have seen that these timestamps are still strings. Use pd.to_datetime to convert the column from strings to DateTime objects.
print(df['timeStamp'][0])
# 2015-12-10 17:40:00 format
df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='%Y-%m-%d %H:%M:%S')
print(type(df['timeStamp'][0]))
print(df['timeStamp'].value_counts())

# use .apply() to create 3 new columns called Hour, Month, and Day of Week.
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.day_of_week)
print(df[['timeStamp', 'Month', 'Hour']].head())

# Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week:
# dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
# df['Day of Week'].replace(dmap, inplace=True)
print(df['Day of Week'].head())
print(df['Day of Week'].value_counts())

# Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
sns.countplot(data=df, x='Day of Week', hue='Reason')
plt.show()

# Now do the same for Month
sns.countplot(data=df, x='Month', hue='Reason')
plt.show()

# You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas...

# Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame.
byMonth = df.groupby('Month').count()
byMonth.reset_index(inplace=True)
print(byMonth.head())

# Now create a simple plot off of the dataframe indicating the count of calls per month
pt1 = df.groupby('Month').count()['lat'].plot()
plt.show()

# Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column.
sns.lmplot(data=byMonth, x='Month', y='lat')
plt.show()

# Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method.
df['Date'] = df['timeStamp'].apply(lambda x: x.date())
print(df['Date'].head())
df['Time'] = df['timeStamp'].apply(lambda x: x.time())
print(df['Time'].head())

# Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.
byDate = df.groupby('Date').count()
byDate['lat'].plot()
plt.show()

# Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()

df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()

df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
plt.tight_layout()
plt.show()

# Now let's move on to creating heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an unstack method. Reference the solutions if you get stuck on this!
mat = df.pivot_table(index='Day of Week', columns='Hour', values='lat', aggfunc='count')
print(mat)
mat1 = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
print(mat1)

# Now create a HeatMap using this new DataFrame.
sns.heatmap(mat)
plt.show()

# Now create a clustermap using this DataFrame.
sns.clustermap(mat)
plt.show()

# Now repeat these same plots and operations, for a DataFrame that shows the Month as the column.
mat2 = df.pivot_table(index='Day of Week', columns='Month', values='lat', aggfunc='count')
print(mat2)

sns.heatmap(mat2)
plt.show()

sns.clustermap(mat2)
plt.show()