from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/statistics')
def statistics():
    with open('day_statistics.json') as json_file:
        data_day = json.load(json_file)
    with open('week_statistics.json') as json_file:
        data_week = json.load(json_file)
    with open('month_statistics.json') as json_file:
        data_month = json.load(json_file)
    data = {
        "day": data_day['day'],
        "week": data_week['week'],
        "month": data_month['month']
    }
    return render_template('statistics.html', data=data)


@app.route('/screen-time')
def screen_time():
    with open('screen_time.json') as json_file:
        data = json.load(json_file)
    first_awake = int(data["firstAwake"] / 60)
    first_awake_hours = int(first_awake / 60)
    first_awake_minutes = int(first_awake % 60)
    hours = f"{first_awake_hours}"
    minutes = f"{first_awake_minutes}"
    if first_awake_hours < 10:
        hours = f"0{first_awake_hours}"
    if first_awake_minutes < 10:
        minutes = f"0{first_awake_minutes}"
    data["firstAwake"] = f"{hours}:{minutes}"

    last_awake = int(data["lastAwake"] / 60)
    last_awake_hours = int(last_awake / 60)
    last_awake_minutes = int(last_awake % 60)
    hours = f"{last_awake_hours}"
    minutes = f"{last_awake_minutes}"
    if last_awake_hours < 10:
        hours = f"0{last_awake_hours}"
    if last_awake_minutes < 10:
        minutes = f"0{last_awake_minutes}"
    data["lastAwake"] = f"{hours}:{minutes}"
    return render_template('screen_time.html', data=data)


@app.route('/real-time')
def real_time():
    with open('real_time.json') as json_file:
        data = json.load(json_file)
    if not data['isScreenOn']:
        time = int(data["timeInfo"] / 60)
        time_hours = int(time / 60)
        time_minutes = int(time % 60)
        hours = f"{time_hours}"
        minutes = f"{time_minutes}"
        if time_hours < 10:
            hours = f"0{time_hours}"
        if time_minutes < 10:
            minutes = f"0{time_minutes}"
        data["timeInfo"] = f"{hours}:{minutes}"

    return render_template('real_time.html', data=data)


# GET requests will be blocked
@app.route('/json-day', methods=['POST'])
def json_day():
    request_data = request.get_json()
    if request_data:
        with open('day_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-week', methods=['POST'])
def json_week():
    request_data = request.get_json()
    if request_data:
        with open('week_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-month', methods=['POST'])
def json_month():
    request_data = request.get_json()
    if request_data:
        with open('month_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-screen-time', methods=['POST'])
def json_screen_time():
    request_data = request.get_json()
    if request_data:
        with open('screen_time.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-real-time', methods=['POST'])
def json_real_time():
    request_data = request.get_json()
    if request_data:
        with open('real_time.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


if __name__ == '__main__':
    app.run(debug=True)