# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Set up plot style
sns.set_style('whitegrid')

# Import data
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.info())

# Plot 1
from scipy import stats
p1 = sns.jointplot(data=titanic, x='fare', y='age')
plt.show()

# Plot 2 - change y axis ticks frequency and x axis limits
p2 = sns.jointplot(data=titanic, x='fare', y='age', xlim=[-100, 500])
p2.ax_joint.set_yticks(list(range(0, 81, 20)))
plt.show()

# Plot 3 - distplot
p3 = sns.distplot(titanic['fare'], bins=30, kde=False, color='red')
plt.show()

# Plot 4 - boxplot
p4 = sns.boxplot(data=titanic, x='class', y='age', palette='rainbow')
plt.show()

# Plot 5 - swarm plot
pt5 = sns.swarmplot(data=titanic, x='class', y='age')
plt.show()

# Plot 6 - countplot
pt6 = sns.countplot(x='sex',data=titanic)
plt.show()

# Plot 7 - heatmap
corr = titanic.corr()
# pt7 = sns.heatmap(titanic.corr(), cmap='coolwarm')
# plt.show()

# Plot 8 - FacetGrid
g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist,'age')
plt.show()
