from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route("/test", methods = ['POST', 'GET'])
def home():
    return "Hello World! its keshav"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
