from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/statistics')
def statistics():
    with open('json_files/day_statistics.json') as json_file:
        data_day = json.load(json_file)
        print(data_day['info'])
    with open('json_files/week_statistics.json') as json_file:
        data_week = json.load(json_file)
    with open('json_files/month_statistics.json') as json_file:
        data_month = json.load(json_file)

    for i in range(1, len(data_day['info']) + 1):
        data_day['info'][i-1]['number'] = i
        duration = int(data_day['info'][i-1]["usageDuration"] / 60)
        duration_hours = int(duration / 60)
        print(duration_hours)
        duration_minutes = int(duration % 60)
        print(duration_minutes)
        hours = f"{duration_hours}"
        minutes = f"{duration_minutes}"
        if duration_hours < 10:
            hours = f"0{duration_hours}"
        if duration_minutes < 10:
            minutes = f"0{duration_minutes}"
        print(data_day['info'][i-1]["usageDuration"])
        data_day['info'][i-1]["usageDuration"] = f"{hours}:{minutes}"
    for i in range(1, len(data_week['info']) + 1):
        data_week['info'][i-1]['number'] = i
        duration = int(data_week['info'][i - 1]["usageDuration"] / 60)
        duration_hours = int(duration / 60)
        duration_minutes = int(duration % 60)
        hours = f"{duration_hours}"
        minutes = f"{duration_minutes}"
        if duration_hours < 10:
            hours = f"0{duration_hours}"
        if duration_minutes < 10:
            minutes = f"0{duration_minutes}"
        data_week['info'][i - 1]["usageDuration"] = f"{hours}:{minutes}"
    for i in range(1, len(data_month['info']) + 1):
        data_month['info'][i-1]['number'] = i
        duration = int(data_month['info'][i - 1]["usageDuration"] / 60)
        duration_hours = int(duration / 60)
        duration_minutes = int(duration % 60)
        hours = f"{duration_hours}"
        minutes = f"{duration_minutes}"
        if duration_hours < 10:
            hours = f"0{duration_hours}"
        if duration_minutes < 10:
            minutes = f"0{duration_minutes}"
        data_month['info'][i - 1]["usageDuration"] = f"{hours}:{minutes}"

    data = {
        "day": data_day['info'],
        "week": data_week['info'],
        "month": data_month['info']
    }
    return render_template('statistics.html', data=data)


@app.route('/screen-time')
def screen_time():
    with open('json_files/screen_time.json') as json_file:
        data = json.load(json_file)

    time = data['totalTime']
    hours = int(time / 3600)
    minutes = int((time - hours*3600) / 60)
    seconds = int((time - hours*3600) - minutes*60)

    data['hours'] = hours
    data['minutes'] = minutes
    data['seconds'] = seconds

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
    with open('json_files/real_time.json') as json_file:
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
        with open('json_files/day_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-week', methods=['POST'])
def json_week():
    request_data = request.get_json()
    if request_data:
        with open('json_files/week_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-month', methods=['POST'])
def json_month():
    request_data = request.get_json()
    if request_data:
        with open('json_files/month_statistics.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-screen-time', methods=['POST'])
def json_screen_time():
    request_data = request.get_json()
    if request_data:
        with open('json_files/screen_time.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/json-real-time', methods=['POST'])
def json_real_time():
    request_data = request.get_json()
    if request_data:
        with open('json_files/real_time.json', 'w') as f:
            json.dump(request_data, f)
        return "Это успех, молодой человек!"
    return "Вот незадача! Неудача!"


@app.route('/get_values', methods=['GET'])
def get_values():
    with open('json_files/real_time.json') as json_file:
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

    return data


if __name__ == '__main__':
    app.run(debug=True)