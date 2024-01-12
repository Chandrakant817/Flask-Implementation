from flask import Flask

app = Flask(__name__)

@app.route("/",methods = ["Get"])
def welcome():
    #return "Welcome Chandrakant Thakur!! "
    return "<h1> Welcome Chandrakant Thakur!! </h1>"

@app.route("/index", methods = ["Get"])
def index():
    #return "welcome to the Index Page"
    return "<h2> welcome to the Index Page </h2>"

if __name__ == "__main__":
    app.run(debug=True)


