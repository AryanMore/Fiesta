import pandas as pd
import numpy as np
import json
import math
# Load your dataset
mama_earth_data = pd.read_csv('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/Reviews Data.csv')
mama_earth_data = mama_earth_data[~mama_earth_data.index.duplicated(keep='first')]
#print(mama_earth_data.head())




mama_earth_data['REVIEW_DATE'] = pd.to_datetime(mama_earth_data['REVIEW_DATE'])

# Create a new column to store the season
mama_earth_data['SEASON'] = ''

# Define the conditions to classify the seasons
winter_condition = (mama_earth_data['REVIEW_DATE'].dt.month.isin([10, 11, 12, 1]))
summer_condition = (mama_earth_data['REVIEW_DATE'].dt.month.isin([2, 3, 4, 5]))
monsoon_condition = (mama_earth_data['REVIEW_DATE'].dt.month.isin([6, 7, 8, 9]))
unknown_condition = ~(winter_condition | summer_condition | monsoon_condition)

# Assign seasons based on conditions
mama_earth_data.loc[winter_condition, 'SEASON'] = 'Winter'
mama_earth_data.loc[summer_condition, 'SEASON'] = 'Summer'
mama_earth_data.loc[monsoon_condition, 'SEASON'] = 'Monsoon'
mama_earth_data.loc[unknown_condition, 'SEASON'] = 'Unknown'

# Print the count of reviews in each season
season_counts = mama_earth_data['SEASON'].value_counts()

product_s = 0
product_w = 0
product_r = 0

category_s = 0
category_w = 0
category_r = 0

##Adding all the product category season wise count in dictionaries

trends_cat = dict()

for c , k in zip(mama_earth_data['PRODUCT_CATEGORY'] , mama_earth_data['SEASON']):
   c = c.replace(" " , "")
   if(k in trends_cat and c in trends_cat[k]):
      trends_cat[k][c] += 1
   else:
      if(k in trends_cat):
        trends_cat[k][c] = 1
      else:
         trends_cat[k] = dict()

for season, categories in trends_cat.items():
    trends_cat[season] = dict(sorted(categories.items(), key=lambda item: item[1]))


#print(trends_cat)

for i , j in zip(mama_earth_data['SKU'] , mama_earth_data['SEASON']):
  if(i == '8906087770534'):
    if(j == 'Winter'): product_w+=1
    elif(j == 'Summer'): product_s+=1
    elif(j == 'Monsoon'): product_r+=1

total_sales_pp = product_r+product_s+product_w
print("Winter Sales are {0} Summer Sales are {1} Monsoon Sales are {2}".format((product_w/total_sales_pp)*100 , (product_s/total_sales_pp)*100 , (product_r/total_sales_pp)*100))


#print(season_counts)
#print(mama_earth_data.head())



# Step 2: Prepare your data (a dictionary in this case)
my_data = {
    "Winter": round((product_w/total_sales_pp)*100),
    "Summer": round((product_s/total_sales_pp)*100),
    "Monsoon": round((product_r/total_sales_pp)*100),
}

# Creating JSON file for the display of trends of products wrt to seasons
with open('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/horizon_tail_wind/src/variables/trends.json', 'w') as json_file:
    # Step 4: Dump your data into the file
    json.dump(my_data, json_file)


#Creating JSON file for the permenenat display of category data
with open('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/horizon_tail_wind/src/variables/trends_category.json', 'w') as json_file:
    # Step 4: Dump your data into the file
    json.dump(trends_cat, json_file)


