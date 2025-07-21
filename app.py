from flask import Flask, render_template, request, redirect, url_for, session
from hungman_word import get_words_by_difficulty
from hungman_art import logo, stages
import random

app = Flask(__name__)
app.secret_key = 'supersecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    username = request.form['username']
    difficulty = request.form['difficulty']
    word_list = get_words_by_difficulty(difficulty)
    word = random.choice(word_list)
    session['username'] = username
    session['difficulty'] = difficulty
    session['word'] = word
    session['guessed'] = []
    session['lives'] = 6
    return redirect(url_for('game'))

@app.route('/game')
def game():
    word = session['word']
    guessed = session['guessed']
    display = ' '.join([letter if letter in guessed else '_' for letter in word])
    stage = stages[6 - session['lives']]
    return render_template('game.html', display=display, guessed=guessed, lives=session['lives'], stage=stage)

@app.route('/guess', methods=['POST'])
def guess():
    letter = request.form['letter'].lower()
    guessed = session['guessed']
    word = session['word']

    if letter not in guessed:
        guessed.append(letter)
        if letter not in word:
            session['lives'] -= 1

    session['guessed'] = guessed

    if session['lives'] == 0 or all([l in guessed for l in word]):
        return redirect(url_for('result'))

    return redirect(url_for('game'))

@app.route('/result')
def result():
    word = session['word']
    guessed = session['guessed']
    won = all([l in guessed for l in word])
    return render_template('result.html', word=word, guessed=guessed, won=won, logo=logo)

if __name__ == '__main__':
    app.run(debug=True)
