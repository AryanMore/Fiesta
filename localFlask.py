import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv('Backend.csv')
df.fillna('', inplace=True)  # Replace NaN values with empty strings or any other appropriate value

@app.route('/api/mamaearth', methods=['GET'])
def get_data():
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
