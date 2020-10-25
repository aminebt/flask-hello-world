# ------ Flask Hello World ------ #
from flask import Flask 

ref_name = "amine"

app = Flask(__name__)
app.config["DEBUG"]=True


@app.route("/")
def main_page():
	return "This is the main page"

@app.route("/hello")
def hello_world():
	return "Hello World?!?!?!?!?!?!?!" 

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print(value+1)
	print(type(value))
	return "correct integer"

@app.route("/float/<float:value>")
def float_type(value):
	print(value+1)
	print(type(value))
	return "correct float"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	print(type(value))
	return "correct path" 

@app.route("/name/<name>")
def right_name(name):
	if name.lower() == ref_name:
		return "Hello, {}".format(name), 200
	else: 
		return "Wrong name", 400



# def main_page():
# 	return "This is the main page"

#start the development server using the run command 
if __name__ == "__main__":
	app.run()

