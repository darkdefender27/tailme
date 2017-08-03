#!coverfox.ass/bin/python

import os
import tailer
from flask import render_template, abort, request
from jinja2 import TemplateNotFound
from app import app, sockets

SLEEP_INTERVAL = 1.0


@app.route('/')
@app.route('/index')
def index():
    try:
        log_dir = app.config['LOG_FOLDER']
        logs = [fname for fname in next(os.walk(log_dir))[2]]
        return render_template('index.html', logs=logs)
    except TemplateNotFound:
        abort(404)


@sockets.route('/tailme')
def echo_socket(ws):
    while True:
        message = ws.receive()
        print message
        ws.send(message[::-1])


@app.route('/taillog', methods=['POST'])
def tail_log():
    selected_log_filename = request.form.get('selected_log')
    log_file = os.path.join(app.config['LOG_FOLDER'], selected_log_filename)
    print "Log: ", log_file
    # Follow the file as it grows
    #for line in tailer.follow(open(log_file)):
    with open(log_file, 'r') as fin:
        for line in readlines_then_tail(fin):
            print "Edit: ", line.strip()
            socketio.emit('newtaildata', {'data': line.strip()},
                namespace='/tailme')


def readlines_then_tail(fin):
    "Iterate through lines and then tail for further lines."
    while True:
        line = fin.readline()
        if line:
            yield line
        else:
            tail(fin)


def tail(fin):
    "Listen for new lines added to file."
    while True:
        where = fin.tell()
        line = fin.readline()
        if not line:
            time.sleep(SLEEP_INTERVAL)
            fin.seek(where)
        else:
            yield line


#
# @socketio.on('taillogs', namespace='/tailme')
# def ws_tail(message):
#     print "Message: ", message
#     tailedLogFilename = message['tailedLogFile']
#     print "Tailing: ", tailedLogFilename
#     log_file = os.path.join(app.config['LOG_FOLDER'], tailedLogFilename)
