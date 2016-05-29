# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
data = []
distances = []
dataPoint = []
def readcsv(fileName):
	rows = None
	f = open(fileName)
	for line in f:
		data.append(line.split(','))

def euclideanDistance(trainSample, testSample):
	sum = (int(trainSample[1])-testSample[0])**2 + (int(trainSample[2])-testSample[1])**2 + (int(trainSample[3])-testSample[1])**2
	return math.sqrt(sum)


def knn():
	for trainSample in data:
		distances.append((euclideanDistance(trainSample, dataPoint),10-int(trainSample[5]),trainSample[0]))
	distances.sort()
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
	# return 'Hello World!'
    return render_template('startpage.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/results', methods=['POST'])
def results():
	return 'hello'
    # name=request.form['yourname']
    # email=request.form['youremail']
    # return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
	app.debug = True
  	app.run()
  
