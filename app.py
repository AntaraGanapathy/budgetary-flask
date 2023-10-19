from flask import Flask, render_template, url_for, redirect, request
from pip._vendor import requests

app = Flask(__name__)
API_KEY = 'S1HTWWB10I1LB5VA'

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

@app.route('/activities/forex-calculator', methods=['GET', 'POST'])
def activity3():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            amount = float(amount)
            from_c = request.form['from_c']
            to_c = request.form['to_c']
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
                from_c, to_c, API_KEY)
            response = requests.get(url=url).json()
            rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
            rate = float(rate)
            result = rate * amount
            from_c_code = response['Realtime Currency Exchange Rate']['1. From_Currency Code']
            from_c_name = response['Realtime Currency Exchange Rate']['2. From_Currency Name']
            to_c_code = response['Realtime Currency Exchange Rate']['3. To_Currency Code']
            to_c_name = response['Realtime Currency Exchange Rate']['4. To_Currency Name']
            time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
            return render_template('activity3.html', result=round(result, 2), amount=amount,
                                   from_c_code=from_c_code, from_c_name=from_c_name,
                                   to_c_code=to_c_code, to_c_name=to_c_name, time=time)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
  
    else:
        return render_template('activity3.html')

@app.route('/activities/savings-target-calculator')
def activity4():
    return render_template('activity4.html')

@app.route('/activities/sip-calculator')
def activity5():
    return render_template('activity5.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)