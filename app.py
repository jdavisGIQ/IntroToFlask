from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = "Malia"
    projectList = ["Tic Tac Toe", "Rock Paper Scissors", "Build Deck", "Palindrome Searcher", "Turtle Art", "Bitmaps", "Platformer Game"]
    return render_template('index.html', title="Index Page", username=name, projectList=projectList)

@app.route('/name')
def displayName():
    return "Malia"

@app.route('/dashboard/<name>')
def dashboard(name):
    return 'Welcome ' + str(name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', name=user))
    else:
        return render_template('login.html', title="Login Page")

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/journalentry', methods=['POST', 'GET'])
def showEntry():
    if request.method == 'POST':
        entry = request.form
        return render_template('journalEntry.html', entry=entry)

@app.route('/upload', methods=['POST', 'GET'])
def uploadFile():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        return 'File Upload Successful'
    else:
        return render_template('fileUpload.html')

app.run(debug=True)