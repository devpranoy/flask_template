# importing packages
from flask import Flask ,render_template, redirect, url_for, session, request, logging
import requests
app = Flask(__name__) #app initialisation

@app.route('/', methods=['GET','POST']) #landing page intent
def home():
    return render_template("index.html") #display the html template

if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=8000) 
    #use threaded=True instead of debug=True for production
    # use port =80 for using the http port

