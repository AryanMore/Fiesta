"""import pandas as pd
import json
from textblob import TextBlob

# Load the dataset
df = pd.read_csv('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/Reviews Data_Origial.csv')

# Drop rows with missing values in 'REVIEW_CONTENT'
df = df.dropna(subset=['REVIEW_CONTENT'])

# Function to perform sentiment analysis for each product category
def perform_sentiment_analysis(category_df):
    # Assign labels based on sentiment polarity
    category_df['LABEL'] = pd.cut(category_df['REVIEW_CONTENT'].apply(lambda x: TextBlob(str(x)).sentiment.polarity),
                                  bins=[-float('inf'), -0.1 , 0.1, float('inf')],
                                  labels=['Negative', 'Neutral', 'Positive'],
                                  include_lowest=True)

    # Count the occurrences of each sentiment label
    sentiment_counts = category_df['LABEL'].value_counts().to_dict()

    # Calculate percentages
    total_reviews = category_df.shape[0]
    positive_percent = round(sentiment_counts.get('Positive', 0) / total_reviews * 100)
    neutral_percent = round(sentiment_counts.get('Neutral', 0) / total_reviews * 100)
    negative_percent = round(sentiment_counts.get('Negative', 0) / total_reviews * 100)

    # Prepare the JSON data structure with percentages
    category_data = {
        'Positive': positive_percent,
        'Neutral': neutral_percent,
        'Negative': negative_percent
    }

    return category_data

# Apply sentiment analysis for each product category and store the results in a dictionary
results = {}
for category, category_df in df.groupby('PRODUCT_CATEGORY'):
    category = category.strip()
    if category not in results:
        results[category] = perform_sentiment_analysis(category_df)

# Write the results to a JSON file
with open('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/horizon_tail_wind/src/variables/sentiment_analysis_results.json', 'w') as f:
    json.dump(results, f, indent=4)

print("JSON file generated successfully!")
"""
import pandas as pd
import plotly.express as px
import json
from collections import OrderedDict

mama_earth_data = pd.read_csv('C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/Reviews Data_Origial.csv')

mama_earth_data['REVIEW_DATE'] = pd.to_datetime(mama_earth_data['REVIEW_DATE'])
#mama_earth_data.set_index('REVIEW_DATE', inplace=True)  # Set 'REVIEW_DATE' as the index
id = "8906087770534"
monthWise_reviews = dict()

for index , sku in enumerate(mama_earth_data['SKU']):
    if(sku == id):
        month = mama_earth_data['REVIEW_DATE'][index].month
        review_Count = mama_earth_data['REVIEW_COUNT'][index]
        if(not mama_earth_data['REVIEW_COUNT'].empty):
            if(month in monthWise_reviews):
                monthWise_reviews[month] += review_Count
            else:
                monthWise_reviews[month] = review_Count
print("DOne")
months = list(monthWise_reviews.keys())
months.sort()
sortedMonths = {i: monthWise_reviews[i] for i in months}
print(sortedMonths)

with open("C:/Users/Kamalkant More/Documents/Hackathon_work/Fiesta/horizon_tail_wind/src/variables/monthly_review.json" , 'w') as json_File:
    json.dump(sortedMonths, json_File)

#Drop duplicate timestamps (if any)
#mama_earth_data = mama_earth_data[~mama_earth_data.index.duplicated(keep='first')]

#monthly_review_count = mama_earth_data.resample('M').size().reset_index(name='Review Count')
#print(monthly_review_count)


