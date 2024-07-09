# Import pandas as pd
import pandas as pd

# Read Salaries.csv as a dataframe called sal
sal = pd.read_csv('Salaries.csv')

# Show dataframe head
print(sal.head())

# Show dataframe info
print(sal.info())

# What is the average BasePay
print(sal['BasePay'].mean())

# What is the highest amount of OvertimePay in the dataset?
print(sal['OvertimePay'].max())

# What is the job title of JOSEPH DRISCOLL ?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

# How much does JOSEPH DRISCOLL make (including benefits)?
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

# What is the name of the highest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()].loc[:, 'BasePay':'TotalPayBenefits'])

# What is the name of the lowest paid person (including benefits)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()].loc[:, 'BasePay':'TotalPayBenefits'])

# What is the average BasePay of all employees per year? 2011-2014
print(sal[['Year', 'BasePay']].groupby('Year').mean())

# How many unique job titles are there?
print(sal['JobTitle'].nunique())

# What are the top 5 most common jobs?
print(sal['JobTitle'].value_counts()[:5])

# How many job titles were represented by only one person in 2013?
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# How many people have the word Chief in their job title?
counter = 0
for title in sal['JobTitle']:
    if 'chief' in title.lower() or 'chief,' in title.lower():
        counter += 1
print(counter)

# Is there a correlation between length of the job title string and salary?
sal['title_length'] = sal['JobTitle'].apply(len)
print(sal['title_length'][:5])
print(sal[['title_length', 'TotalPayBenefits']].corr())
sal['title_length'] = sal['JobTitle'].apply(lambda x: len(x))
print(sal['title_length'][:5])
print(sal[['title_length', 'TotalPayBenefits']].corr())
