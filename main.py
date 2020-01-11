from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Sample app for testing CI/CD of gitlab, testing has nothing to do with the flask"


if __name__ == '__main__':
    app.run()
