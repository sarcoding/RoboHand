from flask import Flask, render_template, redirect, url_for, request
from Controller import hand_tracker, manual_changer
from cvzone.SerialModule import SerialObject

app = Flask(__name__)

curr_status = [1, 1, 1, 1, 1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    hand_tracker()
    return redirect(url_for('index'))

@app.route('/manual')
def manual():
    return render_template("manual_index.html")

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    button_value = request.form['button_value']
    manual_changer(int(button_value))
    return redirect(url_for('manual'))

if __name__ == '__main__':
    app.run(debug=True)