# Import pandas as pd
import pandas as pd

# Read in Ecommerce Purchases csv file
ecom = pd.read_csv('Ecommerce Purchases.txt')

# Check the head of the dataframe
print(ecom.head())

# How many rows and columns are there?
print(ecom.info())
print(ecom.shape)

# What is the average purchase price?
print(ecom['Purchase Price'].mean())

# What is the highest and lowest purchase prices?
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())

# How many people have English 'en' as their language of choice on the website?
print(len(ecom[ecom['Language'] == 'en']))

# How many people have the job title of Lawyer?
print(len(ecom[ecom['Job'] == 'Lawyer']))

# How many people made the purchase in the AM vs PM?
print(ecom['AM or PM'].value_counts())

# What are the 5 most common job titles?
print(ecom['Job'].value_counts()[:5])

# Someone made a purchase from lot: "90 WT", what was the purchase price for this transaction?
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# What is the name of the person with the following credit card number: 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# How many people have American Express as their Credit Card Provider and made a purchase above $95?
print(len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95.0)]))

# How many people have a credit card that expires in 2025?
print(ecom['CC Exp Date'][:5])
counter = 0
for date in ecom['CC Exp Date']:
    if '/25' in date:
        counter += 1
print(counter)

# What are the top 5 most popular email provides?
ecom['Email_provider'] = ecom['Email'].apply(lambda x: x.split('@')[1])
print(ecom['Email_provider'].value_counts()[:5])
