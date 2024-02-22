from flask import Flask, request, jsonify
from flask_cors import CORS
import seasons

app = Flask(__name__)

CORS(app)  # This will enable CORS for all routes

# @app.route('/', methods=["POST","GET"])
# def greetUser():
#     if request.method == "POST":
#         return "POST Method"
#     return "GET Method"
@app.route('/add-category',methods=["POST"])
def addCategory():
    inputs = request.get_json()
    # db call to store ctegory

@app.route('/search-input', methods=["POST"])
def sampleTest():
    searchInput = request.get_json() #input from req.body
    # update json
    #seasons.tp(searchInput)
    print("Search -->", searchInput)
    #seasons.tp(searchInput)
    return {"success":True, "backendPython":"Haha"}

def cdp():
    print("Done reveived the output")
# @app.route('/get-user/<user_id>')
# def get_user(user_id):
#     userData = {
#         "userId" : user_id,
#         "userName" :"Manoj",
#         "email":"mnojs36@gmail.com"
#     }
#     extra = request.args.get("extra")
#     userData["extra"] = extra
#     return jsonify(userData), 200

if __name__ == "__main__":
    app.run(debug=True)
