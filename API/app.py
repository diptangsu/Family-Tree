"""Main app file.
This is the entry point for the entire API.
"""
from flask import Flask, jsonify
from flask_jwt import JWT
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from auth import authenticate, identity
from blueprints import RELATIONS_BLUEPRINT, USERS_BLUEPRINT
from database.db import db
from helpers.http import Response

app = Flask(__name__)

app.config.from_pyfile('config/settings.cfg')
db.init_app(app)

migrate = Migrate(app, db, compare_type=True)
jwt = JWT(app, authenticate, identity)

# register blueprints
app.register_blueprint(USERS_BLUEPRINT, url_prefix='/users')
app.register_blueprint(RELATIONS_BLUEPRINT, url_prefix='/relations')


@app.route("/urls")
def site_map():
    return jsonify(
        sorted(
            [
                ', '.join(rule.methods - {'OPTIONS', 'HEAD'}) + ': ' + rule.rule
                for rule in app.url_map.iter_rules()
                if not rule.rule.startswith('/static')
            ],
            key=lambda r: r.split(':')[1],
        )
    )

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.errorhandler(HTTPException)
def handle_exception(err: HTTPException) -> Response:
    """Global error handler."""
    if err.code is None:
        return Response.error(err.description)
    return Response.error(err.description, status=err.code)


if __name__ == '__main__':
    app.run(debug=True)
