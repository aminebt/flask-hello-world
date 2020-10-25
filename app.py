# ------ Flask Hello World ------ #
from flask import Flask 

app = Flask(__name__)

@app.route("/")
def main_page():
	return "This is the main page"

@app.route("/hello")
def hello_world():
	return "Hello World!" 


# def main_page():
# 	return "This is the main page"

#start the development server using the run command 
if __name__ == "__main__":
	app.run()

