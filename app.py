from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)


# Load timeslots from JSON file
def load_timeslots():
    with open('timeslots.json', 'r') as f:
        return json.load(f)


# Save timeslots to JSON file
def save_timeslots(timeslots):
    with open('timeslots.json', 'w') as f:
        json.dump(timeslots, f, indent=4)


@app.route('/')
def index():
    timeslots = load_timeslots()
    return render_template('index.html', timeslots=timeslots)


@app.route('/book', methods=['POST'])
def book():
    timeslot = request.form['timeslot']
    name = request.form['name']
    attendance_type = request.form['attendance_type']

    timeslots = load_timeslots()
    if timeslots[timeslot]['booked_by'] == "":
        timeslots[timeslot]['booked_by'] = name
        timeslots[timeslot]['attendance_type'] = attendance_type
        save_timeslots(timeslots)
        return redirect(url_for('index'))
    else:
        return "Timeslot already booked!", 400


if __name__ == '__main__':
    app.run(debug=True)
