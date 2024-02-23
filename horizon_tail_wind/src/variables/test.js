//const { keyframes } = require('@emotion/react');
//const category_trends = require('./trends_category.json');
/*
const summer = [];

for(const[key , value] of Object.entries(category_trends))
{
   for(const[k , v] of Object.entries(key))
   {
    summer
   }
}
*/
/*
const seasons = ["Winter", "Summer", "Monsoon"];
const seasonArrays = {
    Winter: [],
    Summer: [],
    Monsoon: [],
  };
  
  seasons.forEach(season => {
    for (const [category, data] of Object.entries(category_trends)) {
      const value = data[season];
      if (value !== undefined && value !== 0) {
        seasonArrays[season].push(value);
      }
    }
  });
  
  // Print the results
  console.log(seasonArrays.Winter);
  console.log(seasonArrays.Summer);
  console.log(seasonArrays.Monsoon);
  */
/*
const unknown = category_trends['Unknown'];
const monsoon = category_trends['Monsoon'];
const summer = category_trends['Summer'];
const winter = category_trends['Winter'];

// Now, let's extract the magic values!
const unknownValues = Object.values(unknown);
const monsoonValues = Object.values(monsoon);
const summerValues = Object.values(summer);
const winterValues = Object.values(winter);
console.log(summerValues);
*/


// Summer, Winter, and Monsoon Analysis of the Product Category
const categorySentiments = require('./sentiment_analysis_results.json');
const sentiments = ["Positive", "Negative", "Neutral"];
var categoriesNames = [];
const sentimentArrays = {
    Positive: [],
    Negative: [],
    Neutral: []
};

sentiments.forEach(sentiment => {
    for (const [category, data] of Object.entries(categorySentiments)) {
        const value = data[sentiment];
        if (value !== undefined && value !== 0) {
            sentimentArrays[sentiment].push(value);
        }
    }
});

// Print the results
console.log("Sentiment Arrays for Positive:", sentimentArrays.Positive);
console.log("Sentiment Arrays for Negative:", sentimentArrays.Negative);
console.log("Sentiment Arrays for Neutral:", sentimentArrays.Neutral);

var i = 0;
for (const [keys, values] of Object.entries(categorySentiments)) {
    if (keys !== 'Other') {
        categoriesNames[i] = keys;
        //console.log(categoriesNames[i]);
        i++;
    }
}
