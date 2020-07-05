from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import requests
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}

@app.route("/")
def index():
    return render_template("index2.html", votes = votes)

@socketio.on("submit vote")
#execute once the event "submite vote" is detected
def vote(data):
    selection = data["selection"]
    """
    emit("announce vote", {"selection": selection}, broadcast = True)
    #similar to socket.emit in html
    #broadcast = Ture -> broadcast to everyone
    """
    votes[selection] += 1
    emit("vote totals", votes, broadcast = True)
