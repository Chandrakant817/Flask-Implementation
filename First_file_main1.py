from flask import Flask

## Creating a simple Flask Application
app = Flask(__name__) #Program entry point


if __name__ == "__main__":
    app.run(debug=True)
