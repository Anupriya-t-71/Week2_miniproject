from flask import flask
app = Flask(_name)

@app.route('/')
def home():
 return "Hello from Jenkins CI/CD Pipeline! Deployed my week 2 project SUCCESSFULYY!!!!!!"

if_name_=='_main_':
 app.run(host='0.0.0.0',port=8080)
