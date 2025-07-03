from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Motivational quotes
quotes = [
    "Be like Kohli – Focused and never giving up!",
    "Work hard today, relax like it's a Sunday chai break!",
    "Do it with desi swag!",
    "Even Mumbai traffic clears up eventually, so keep going!"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        mood = request.form['mood']
        meetings = int(request.form['meetings'])

        schedule = []
        for i in range(1, meetings + 1):
            start = request.form.get(f'meeting_start_{i}', '')
            end = request.form.get(f'meeting_end_{i}', '')
            schedule.append((f"Meeting {i}", f"{start} - {end}"))

        lunch = request.form['lunch']
        schedule.append(("Lunch", f"{lunch} - Meal time"))

        if request.form.get('exercise') == 'yes':
            exercise_time = request.form.get('exercise_time', '')
            if exercise_time:
                schedule.append(("Exercise", f"{exercise_time} - Get up and start running!"))

        sleep = request.form['sleep']
        schedule.append(("Sleep", f"{sleep} - Go to sleep. Sleep well!"))

        mood_msg = "You're on fire today! Keep going!" if mood == "productive" else "Wake up! Take a walk!"
        quote = random.choice(quotes)

        return render_template('result.html', name=name, schedule=schedule, mood_msg=mood_msg, quote=quote)

    return render_template('form.html')


# important for deployment
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
