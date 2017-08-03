from flask.ext.socketio import emit

from app import socketio

@socketio.on('connect', namespace='/tailme')
def test_connect():
    pass

@socketio.on('disconnect', namespace='/tailme')
def test_disconnect():
    pass
