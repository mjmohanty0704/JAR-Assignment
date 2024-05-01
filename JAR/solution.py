
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

# C.1 Analyzing the performance of sales and revenue, January to March across the Product line, Gender, and Payment Method
data['Date'] = pd.to_datetime(data['Date'])
jan_march_data = data[(data['Date'].dt.month >= 1) & (data['Date'].dt.month <= 3)]
jan_march_performance = jan_march_data.groupby(['Product line', 'Gender', 'Payment']).agg({'Quantity': 'sum', 'Unit price': 'sum'})
print("\nPerformance from January to March across Product line, Gender, and Payment Method:")
print(jan_march_performance)
print('--------------------------------------------------------------------------------------------------------------')

# C.2 Identifying potential focus areas based on jan_march_performance
# Finding the overall mean/average revenue
overall_revenue_mean = jan_march_performance['Unit price'].mean()

# Filtering groups with revenue below a certain threshold (overall_revenue_mean * 0.75, considering 75% as our threshold)
low_revenue_areas = jan_march_performance[jan_march_performance['Unit price'] < overall_revenue_mean * 0.75]

# Focusing on groups with the largest decrease from overall data
# Printing the identified focus areas
print("\n**Potential Focus Areas for April based on analysis of data from January-March :")
if not low_revenue_areas.empty:
    print(low_revenue_areas)
else:
    print("Good to go!!!")
print('--------------------------------------------------------------------------------------------------------------')
