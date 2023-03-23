# first hello world application using flask

#flask is module
#Flask is name of the class

from flask import Flask
#create an instance of web server(instantiation)

app = Flask(__name__) # __name__ will get the current module name

# start app on the port
#host = localhost or 0.0.0.0

app.run(host="0.0.0.0",port=4000,debug=True)






