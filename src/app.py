from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add-two-nums', methods=["POST"])
def add_two_nums():
	# Extract x, y from the posted data
	dataDict=request.get_json()


	# Add x+y and store it
	z = dataDict["x"] + dataDict["y"]

	# Prepare json to return the values as 'z'
	return jsonify({"z": z})

@app.route('/')
def hello_world():
	return "Hello World from inside a docker container that is hosted in docker-compoes."

if __name__ == "__main__":
    	app.run(debug=True)
