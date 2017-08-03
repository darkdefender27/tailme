#!coverfox.ass/bin/python

from flask import Flask
from flask.ext.socketio import SocketIO
from flask_sockets import Sockets

app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')

sockets = Sockets(app)

# socketio = SocketIO(app)

from app import views
from app import websockets
