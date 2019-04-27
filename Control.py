from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('myevent')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('arrows')
def handle_message(message):
    print('received message: ' + str(message))

@app.route("/")
def root():
  message = "Hey World"
  return render_template('index.html',message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
    
