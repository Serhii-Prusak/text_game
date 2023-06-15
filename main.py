from flask import Flask, request, redirect, url_for

# FLASK engine
app = Flask(__name__)

@app.route('/')
def start():
    return "You are on your path to something hidden! Are you ready?"
if __name__ == "__main__":
    app.run()