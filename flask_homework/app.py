from flask import Flask, render_template
from flask_restful import abort
from werkzeug.utils import redirect

from flask_homework.fruits.routes import fruits
from flask_homework.home.routes import home
from flask_homework.vegetables.routes import vegetables


app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(vegetables)
app.register_blueprint(fruits)


@app.route('/interesting')
def page_not_implemented():
    abort(404)


@app.errorhandler(404)
def error_404_handler(error):
    return render_template('error.html')


@app.route('/redirect')
def redirect_page():
    return redirect("https://youtu.be/s9APLXM9Ei8")


if __name__ == '__main__':
    app.run(debug=True)
