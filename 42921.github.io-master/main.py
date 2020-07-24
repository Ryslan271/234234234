from flask import Flask, render_template, redirect, request
from flask_restful import abort
from models.users import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ryslan2003vs'


@app.route("/")
def home():
    form = RegisterForm()

    return render_template('index.html', form=form)


@app.errorhandler(400)
def not_found_error(error):
    pass
    # return render_template('Error/400.html'), 400


@app.errorhandler(401)
def not_found_error(error):
    pass
    # return render_template('Error/401.html'), 401


@app.errorhandler(404)
def not_found_error(error):
    pass
    # return render_template('Error/404.html'), 404


@app.errorhandler(500)
def not_found_error(error):
    pass
    # return render_template('Error/500.html'), 500


@app.errorhandler(502)
def not_found_error(error):
    pass
    # return render_template('Error/502.html'), 502


@app.errorhandler(503)
def not_found_error(error):
    pass
    # return render_template('Error/503.html'), 503


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
