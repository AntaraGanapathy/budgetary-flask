from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/activities/compound-simple-interest')
def activity1():
    return render_template('activity1.html')

@app.route('/activities/compound-interest-calculator')
def activity2():
    return render_template('activity2.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)