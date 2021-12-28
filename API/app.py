"""Main app file.
This is the entry point for the entire API.
"""
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt import JWT, current_identity, jwt_required
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from auth import authenticate, identity
from blueprints import RELATIONS_BLUEPRINT, USERS_BLUEPRINT
from database.db import db
from helpers.http import Response

app = Flask(__name__)

app.config.from_pyfile('config/settings.cfg')
db.init_app(app)

CORS(app)
migrate = Migrate(app, db, compare_type=True)
jwt = JWT(app, authenticate, identity)

# register blueprints
app.register_blueprint(USERS_BLUEPRINT, url_prefix='/users')
app.register_blueprint(RELATIONS_BLUEPRINT, url_prefix='/relations')


@app.route('/ping')
def ping():
    """Check if the API is running"""
    return Response.success('pong')


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


@app.route('/protected')
@jwt_required()
def protected():
    return Response.success({'user': str(current_identity)})


@app.errorhandler(HTTPException)
def handle_exception(err: HTTPException) -> Response:
    """Global error handler."""
    if err.code is None:
        return Response.error(err.description)
    return Response.error(err.description, status=err.code)


if __name__ == '__main__':
    app.run(debug=True)
