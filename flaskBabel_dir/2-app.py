from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

#@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.locale_selector_func = get_locale

@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)