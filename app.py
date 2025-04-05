from flask import Flask, render_template, request, jsonify
import random
app = Flask(__name__)

target_number = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.json['guess'])
    if user_guess < target_number:
        return jsonify({'message': 'Too low! Try again.'})
    elif user_guess > target_number:
        return jsonify({'message': 'Too high! Try again.'})
    else:
        return jsonify({'message': '🎉 Correct! You guessed it!'})
    
if __name__ == '__main__':
    app.run(debug=True)
    
# This code is a simple Flask web application that implements a number guessing game.