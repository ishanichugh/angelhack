# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import csv
import math
import json
from flask import send_file

data = []
distances = []
dataPoint = []
finalAns ={}
def readcsv(fileName):
	rows = None
	f = open(fileName)
	for line in f:
		data.append(line.split(','))

def euclideanDistance(trainSample, testSample):
	sum = (float(trainSample[1])-testSample[0])**2 + (float(trainSample[2])-testSample[1])**2 + (float(trainSample[3])-testSample[1])**2
	return math.sqrt(sum)


def knn():
	for trainSample in data:
		distances.append((euclideanDistance(trainSample, dataPoint),10-float(trainSample[5]),trainSample[0]))
	distances.sort()

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('startpage.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello', methods=['POST'])
def hello():
    # firstname=request.form['firstname']
    # lastname=request.form['lastname']
    # finalAns={}
    del dataPoint[:]
    finalAns.clear()
    age=request.form['age']
    waist=request.form['waist']
    height=request.form['height']
    dataPoint.append(float(waist))
    dataPoint.append(float(age))
    dataPoint.append(float(height))
    # email=request.form['youremail']
    # return render_template('form_action.html', name=name, email=email)
    readcsv('marriage.csv')
    knn()
    for i in range(0,20):
    	try:
    		finalAns[distances[i][2]]+=1
    	except Exception, e:
    		finalAns[distances[i][2]] =1
    print finalAns    
    filename = 'shirt-trouser.jpg'
    return '<img src="/home/shrenik/Desktop/app/shirt-trouser.jpg" style="width:304px;height:228px;">'

# Run the app :)
if __name__ == '__main__':
	app.debug = True
  	app.run()