from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a ArgoCD demo, TY from Rohan G!!!'
