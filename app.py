from flask import Flask, render_template, request, redirect, session, url_for, send_from_directory
import random
import time
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

scoreboard = []

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        '64X64.png', mimetype='image/png')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        session['player_name'] = request.form['player_name']
        session['min'] = int(request.form['min_num'])
        session['max'] = int(request.form['max_num'])
        difficulty = request.form['difficulty']

        if difficulty == 'easy':
            session['max_attempts'] = 10
        elif difficulty == 'medium':
            session['max_attempts'] = 7
        elif difficulty == 'hard':
            session['max_attempts'] = 5

        session['number'] = random.randint(session['min'], session['max'])
        session['attempts'] = 0
        session['start_time'] = time.time()
        session['score'] = session.get('score', 0)

        return redirect(url_for('play'))
    return render_template('setup.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'max_attempts' not in session or 'attempts' not in session:
        return redirect(url_for('setup'))

    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
        except ValueError:
            message = "Invalid input. Please enter a number."
            return render_template('play.html', message=message,
                attempts_left=session['max_attempts'] - session['attempts'],
                score=session['score'], min_num=session['min'], max_num=session['max'])

        session['attempts'] += 1

        if guess < session['number']:
            message = 'Too low!'
        elif guess > session['number']:
            message = 'Too high!'
        else:
            end_time = time.time()
            elapsed_time = round(end_time - session['start_time'], 2)
            session['score'] += 10

            scoreboard.insert(0, {
                'name': session['player_name'],
                'guess': guess,
                'number': session['number'],
                'result': 'win',
                'score': session['score'],
                'time': elapsed_time
            })
            if len(scoreboard) > 5:
                scoreboard.pop()

            return render_template('result.html', result='win',
                                   player_name=session['player_name'],
                                   number=session['number'],
                                   time=elapsed_time,
                                   score=session['score'],
                                   scoreboard=scoreboard)

        if session['attempts'] >= session['max_attempts']:
            end_time = time.time()
            elapsed_time = round(end_time - session['start_time'], 2)
            session['score'] -= 5

            scoreboard.insert(0, {
                'name': session['player_name'],
                'guess': guess,
                'number': session['number'],
                'result': 'lose',
                'score': session['score'],
                'time': elapsed_time
            })
            if len(scoreboard) > 5:
                scoreboard.pop()

            return render_template('result.html', result='lose',
                                   player_name=session['player_name'],
                                   number=session['number'],
                                   time=elapsed_time,
                                   score=session['score'],
                                   scoreboard=scoreboard)

    return render_template('play.html', message=message,
        attempts_left=session['max_attempts'] - session['attempts'],
        score=session['score'], min_num=session['min'], max_num=session['max'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
