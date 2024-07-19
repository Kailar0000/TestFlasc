from flask import Flask
from flask import render_template, request, redirect, session

from config import token
from api import get_weather

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET', 'POST'])
def start_page():
    if 'city' in session:
        return redirect(f'/wether_page/{session["city"]}')
    else:
        if request.method == 'POST':
            city = request.form['city']
            session['city'] = city
            return redirect(f'/wether_page/{city}')
    return render_template('home.html')

@app.route("/wether_page/<city>", methods=['GET', 'POST'])
def wether_page(city):
    data = get_weather(city, token)
    location = data["location"]
    if request.method == 'POST':
        city = request.form['city']
        return redirect(f'/wether_page/{city}')
    return render_template('wether.html', data=data)


if __name__ == '__main__':
  app.run(debug=True)