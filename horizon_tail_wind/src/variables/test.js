const category_trends = require('./trends_category.json');
/*
const summer = [];

for(const[key , value] of Object.entries(category_trends))
{
   summer     
}*/

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