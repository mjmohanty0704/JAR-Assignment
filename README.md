# Assignment for Business Analyst Intern @Jar
### 1. Walmart Sales Analysis:
```You have been given a data set to analyze and answer the following questions: 
Please note: You have to use Python to answer the questions.
Data Set: Walmart Sales [Kindly find an attached copy in the email]
```

A. Analyze the performance of sales and revenue at the city and branch level ( 5 marks)

B. What is the average price of an item sold at each branch of the city (10 marks)

C. Analyze the performance of sales and revenue, Month over Month across the Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019. (15 marks)

### Solution
```python
# --------------------------------------------------------------------------------------------------------------
# # To convert .xlsx to .csv
# import pandas as pd

# # Load Excel file
# excel_file = 'walmart_sales.xlsx'
# df = pd.read_excel(excel_file)

# # Save as CSV file
# csv_file = 'walmart_sales.csv'
# df.to_csv(csv_file, index=False)  
# --------------------------------------------------------------------------------------------------------------

import pandas as pd

# Load the dataset
data = pd.read_csv('walmart_sales.csv')

# A. Performance of sales and revenue at the city and branch level
city_branch_level_performance = data.groupby(['City', 'Branch']).agg({'Quantity': 'sum', 'Unit price': 'sum'})
print("Performance at the city and branch level:")
print(city_branch_level_performance)
print('--------------------------------------------------------------------------------------------------------------')

# B. Average price of an item sold at each branch of the city
average_price_per_branch = data.groupby(['City', 'Branch']).agg({'Unit price': 'mean'})
print("\nAverage price of an item sold at each branch of the city:")
print(average_price_per_branch)
print('--------------------------------------------------------------------------------------------------------------')

# C.1 Analyze the performance of sales and revenue, January to March across the Product line, Gender, and Payment Method
data['Date'] = pd.to_datetime(data['Date'])
jan_march_data = data[(data['Date'].dt.month >= 1) & (data['Date'].dt.month <= 3)]
jan_march_performance = jan_march_data.groupby(['Product line', 'Gender', 'Payment']).agg({'Quantity': 'sum', 'Unit price': 'sum'})
print("\nPerformance from January to March across Product line, Gender, and Payment Method:")
print(jan_march_performance)
print('--------------------------------------------------------------------------------------------------------------')

# C.2 Identify potential focus areas based on jan_march_performance
# Find the overall mean/median revenue
overall_revenue_mean = jan_march_performance['Unit price'].mean()

# Filter groups with revenue below a certain threshold (overall_revenue_mean * 0.75, considering 75% as our threshold)
low_revenue_areas = jan_march_performance[jan_march_performance['Unit price'] < overall_revenue_mean * 0.75]

# Focus on groups with the largest decrease from overall data
# Print the identified focus areas
print("\n**Potential Focus Areas for April based on analysis of data from January-March :")
if not low_revenue_areas.empty:
    print(low_revenue_areas)
else:
    print("No significant areas with low revenue identified based on the chosen threshold.")
print('--------------------------------------------------------------------------------------------------------------')
```
---

### 2. App Exploration: (5 marks)
Explore the features and user experience of the Jar app. Identify two aspects that you think could be significantly improved and explain your reasoning behind each suggestion.

**1. Autopay setup:** 

- Considering myself a customer, I feel that this is a very good app to invest in gold, that too on a daily basis, but in our tidious and busy life we might or might not be able to visit the app on a daily basis. So autopay setup option should be given to the user which would enable the customer to debit some amount from his account towards this saving.

**2. Mulitilingual video instructions and new user registration:**

- The videos that provides information regarding the functioning of the app should be provided in Hindi and English so that in future the company can cater international customers as well. 

- Also, if we are focussing on Indian customers only, then the instructions video can be provided in multiple Indian languages.

- When a new user is registering, rather than directly starting to use the app I feel that the user should be sent basic documentation regarding the terms and conditions and the basic "how to" of the app and also attaching the link to the instructions videos so that the app would remain a little uncluttered. 
- We can also put in a basic in-app graphic tutorial for the new registered customers.


### 3. Product Optimisation: (5 marks)
The Jar app has an engagement feature called 'Spin to Win'. Right now, if 100 people come to the app each day, only 23 of them try out this spinning game. But, we know that people who spin are more likely to retain on the app and do transactions. Now, we want to get more people to play the game. So, the question is, how can we make sure that at least 50 people out of every 100 who visit the app each day will play 'Spin to Win'? What can we do to get more people interested in spinning the wheel?

