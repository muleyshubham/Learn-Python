#importing a flask module

from flask import Flask

#start a web server
app=Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return "Hello Everyone!Welcome to first page"

@app.route("/Employees",methods=["GET"])
def employee():
    return "List of Employees are [emp1,emp2,emp3]"

#start the app on the local host on port 4000
app.run(host="0.0.0.0",port=4000,debug=True)