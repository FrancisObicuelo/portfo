from flask import Flask, render_template, request, url_for, redirect
from jinja2 import TemplateNotFound
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>.html')
def render_page(page):
    try:
        return render_template(f"{page}.html")
    except TemplateNotFound:
        return render_template('404.html'), 404

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('./web_server/database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # was GET or the credentials were invalid
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/favicon.ico') #endpoint
# def blog2():
#     return 'this is my dog'

# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> set FLASK_APP="server.py"
# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> python -m flask run
# Usage: python -m flask run [OPTIONS]
# Try 'python -m flask run --help' for help.

# Error: Could not locate a Flask application. Use the 'flask --app' option, 'FLASK_APP' environment variable, or a 'wsgi.py' or 'app.py' file in the current directory.
# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> flask run


# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> $env:FLASK_ENV="development"
# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> $env:FLASK_DEBUG="1"
# PS C:\Users\francisco.ferreira\Desktop\python\py_dev\web_server> flask run

# favicon

