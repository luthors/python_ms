from flask import Flask

app = Flask(__name__)


@app.route("/getWF")
def getWFOnline():
    return "Todau is gonna be a great sunny python programmer"