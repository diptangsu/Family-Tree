"""Separating out the db object so that it can be reused."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
