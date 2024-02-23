import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prathamesh@001",
    database="mamaearth"
)

mycursor = mydb.cursor()

col_names = ['SKU', 'PNAME', 'PRICE','CATEGORY', 'RCOUNT', 'DATE', 'REVIEW']
testFile = pd.read_csv('Backend.csv', names=col_names, header=None, skiprows=1)
testFile = testFile.where(pd.notnull(testFile), None)

def dbInsert():
    for i, row in testFile.iterrows():
        row = row.where(pd.notnull(row), None)
        sql = "INSERT INTO product (SKU, PNAME, PRICE, CATEGORY, RCOUNT, DATE, REVIEW) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        #value = (row['SKU'], row['PNAME'], row['PRICE'],row['CATEGORY'], row['RCOUNT'], row['DATE'], row['REVIEW'])  # Assuming the columns are in the order PRN, NAME, BRANCH
        value = tuple(row)

        #mycursor.execute(sql, value)  # Execute the SQL query
        #mydb.commit()  # Commit the transaction

        # try:
        #     mycursor.execute(sql, value)  # Execute the SQL query
        #     mydb.commit()  # Commit the transaction
        # except mysql.connector.Error as err:
        #     print("Error occurred while inserting row:")
        #     print(row)
        #     print("MySQL Error:", err)


@app.route('/api/mamaearth', methods=['POST','GET'])
def get_data():
    data = testFile.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    dbInsert()  # Call dbInsert function to insert data into the database
    app.run(host='0.0.0.0', debug=True)
