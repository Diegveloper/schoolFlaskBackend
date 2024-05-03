from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
import json
import pprint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
 
@app.route('/')
def ping():
    return "Hi I'm alive"

@app.route('/authorization', methods=['GET'])
def validateToken():
    print("hola")
    #abort(401, "Invalid Token")
    return jsonify({"status":"200"})

@app.route('/students',methods=['GET'])
def getStudent():
    userId = request.args.get('id')
    if "Authorization" not in request.headers:
        abort(401, "no token")
    data = loadData("student.json")
    try:
        for i in data['students']:
            if i['id'] == userId:
                return jsonify(i)
        

    except:
        abort(404, "no token")

    

@app.route('/login',methods=['POST'])
def validateLoginCredentials():
    email = ""
    password = ""
    data = request.json
    #possible scenarios
    #empty payload though flask returns a 415 in case there is no payload
    if(not request.data):
        print("there is no payload")
    #not the right amount of arguments on the payload 
    if( len(data) > 2):
        abort(400, description="Bad request, wrong number of arguments")
    #wrong arguments 
    try:
        email = data['email']
        password = data['password'] 
    except: 
        abort(400, description="Bad request, wrong arguments")
    #matching values
    if email == "diego@email.com" and password == "1234":
        data = loadData("LoginResponse.json")
        return jsonify(data)
    else:
        abort(401, "Invalid credentials")




def loadData(fileName):
    with open(fileName,'r') as file:
        data = file.read()
        
    return json.loads(data)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="3000")