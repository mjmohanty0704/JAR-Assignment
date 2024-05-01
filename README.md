# Assignment for Business Analyst Intern @Jar
## 1. Walmart Sales Analysis:
```You have been given a data set to analyze and answer the following questions: 
Please note: You have to use Python to answer the questions.
Data Set: Walmart Sales [Kindly find an attached copy in the email]
```

**A. Analyze the performance of sales and revenue at the city and branch level ( 5 marks)**

**B. What is the average price of an item sold at each branch of the city (10 marks)**

**C. Analyze the performance of sales and revenue, Month over Month across the Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019. (15 marks)**

### Solution (Code)
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
### Solution (Output)
```
Performance at the city and branch level:
                  Quantity  Unit price
City      Branch                      
Mandalay  A            637     6349.11
          B            664     6623.73
          C            519     5506.04
Naypyitaw A            648     5953.55
          B            604     6298.64
          C            579     6315.57
Yangon    A            598     6342.88
          B            631     6329.25
          C            630     5953.36
--------------------------------------------------------------------------------------------------------------

Average price of an item sold at each branch of the city:
                  Unit price
City      Branch            
Mandalay  A        53.353866
          B        56.133305
          C        57.958316
Naypyitaw A        54.123182
          B        57.785688
          C        57.941009
Yangon    A        55.639298
          B        56.011062
          C        52.684602
--------------------------------------------------------------------------------------------------------------

Performance from January to March across Product line, Gender, and Payment Method:
                                           Quantity  Unit price
Product line           Gender Payment                          
Electronic accessories Female Cash              206     2092.11
                              Credit card       149     1348.11
                              Ewallet           133      932.11
                       Male   Cash              192     1602.72
                              Credit card       113     1102.17
                              Ewallet           178     2026.55
Fashion accessories    Female Cash              160     1637.47
                              Credit card       173     1763.62
                              Ewallet           197     1929.50
                       Male   Cash              120     1846.14
                              Credit card       120     1365.06
                              Ewallet           132     1631.56
Food and beverages     Female Cash              183     2102.79
                              Credit card       171     1753.62
                              Ewallet           160     1551.72
                       Male   Cash              112     1366.12
                              Credit card       164     1575.62
                              Ewallet           162     1395.67
Health and beauty      Female Cash              120     1137.15
                              Credit card       111      903.65
                              Ewallet           112     1228.91
                       Male   Cash              173     1479.23
                              Credit card       163     1890.63
                              Ewallet           175     1698.31
Home and lifestyle     Female Cash              147     1433.99
                              Credit card       174     1351.60
                              Ewallet           177     1736.57
                       Male   Cash              159     1497.66
                              Credit card        85      871.02
                              Ewallet           169     1959.87
Sports and travel      Female Cash              188     1720.23
                              Credit card       150     1432.07
                              Ewallet           158     1632.02
                       Male   Cash              136     1609.48
                              Credit card       149     1559.51
                              Ewallet           139     1507.57
--------------------------------------------------------------------------------------------------------------

**Potential Focus Areas for April based on analysis of data from January-March :
                                           Quantity  Unit price
Product line           Gender Payment                          
Electronic accessories Female Ewallet           133      932.11
                       Male   Credit card       113     1102.17
Health and beauty      Female Cash              120     1137.15
                              Credit card       111      903.65
Home and lifestyle     Male   Credit card        85      871.02
--------------------------------------------------------------------------------------------------------------
```

## 2. App Exploration: (5 marks)
**Explore the features and user experience of the Jar app. Identify two aspects that you think could be significantly improved and explain your reasoning behind each suggestion.**

**1. Autopay setup:** 

- As a customer, I believe that this is an excellent tool for gold investing. But, due to our hectic and meticulous lives, we may not always be able to access the app. Therefore, the user should have the ability to set up autopay, which would allow the customer to debit a portion of his account towards this savings.

**2. Mulitilingual video instructions and new user registration:**

- To eventually serve customers from other nations, the app's developer should offer both Hindi and English versions of the instructional films. 

- If our main target market is Indian customers, we can provide the instructions video in many Indian languages.

- I think that new users should receive some basic material in their registered email address so they can learn about the terms and conditions and how to work with the app, rather than having them access it immediately after registration. To keep the app fairly tidy, they should also receive a link to the basic instructional videos in the documentation itself. 

- A basic in-app visual instruction may also be included for newly registered users.



## 3. Product Optimisation: (5 marks)
**The Jar app has an engagement feature called *'Spin to Win'*. Right now, if 100 people come to the app each day, only 23 of them try out this spinning game. But, we know that people who spin are more likely to retain on the app and do transactions. Now, we want to get more people to play the game. So, the question is, how can we make sure that at least 50 people out of every 100 who visit the app each day will play 'Spin to Win'? What can we do to get more people interested in spinning the wheel?**

1. **Promotional Campaigns:**
   - Run campaigns to entice users to play the "Spin to Win" game within the app, via push notifications, or through email marketing. Provide benefits for playing the game, such as bonus points or exclusive rewards.
   - Promote the advantages of engaging in the game, like the elevated chance of obtaining rewards, accessing special deals, or earning loyalty points.

2. **Personalized Recommendations:**
   - Examine user behaviour and preferences using machine learning techniques and data analytics. Users who are more likely to be interested in playing the game should receive personalized recommendations or targeted messaging based on their previous app usage.
   - Divide users into various categories, then customize incentives or promotional offers based on the interests and preferences of each group.

3. **Social Sharing tools and Referral Programs:**
   - Include social sharing tools in the app so that users may tell their friends and social networks about their gaming accomplishments. Provide incentives or benefits to players who suggest friends to join the game.
   - Make viral marketing campaigns or challenges that allow consumers to play the "Spin to Win" game and challenge their friends to beat their high scores.

4. **Limited-Time Events and Prizes:**
   - Arrange one-time events or unique promotions where users can play the "Spin to Win" game to win special prizes or awards. For more users to participate throughout the event duration, create a sense of urgency and enthusiasm.
   - To increase player appeal, add holiday-themed events or seasonal themes to the game.


-  *Also various similar games can be included in the app to upthrust the interest of the customers but the games should not be too much of a distraction.*

