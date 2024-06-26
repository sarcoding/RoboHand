from flask import Flask, render_template, redirect, url_for
from hand_tracker import hand_tracker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    hand_tracker()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)