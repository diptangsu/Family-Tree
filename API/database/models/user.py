from datetime import datetime
from typing import Set
from database.models._crud import CRUDMixin
from sqlalchemy import or_

import bcrypt

from database import db


class User(CRUDMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.Column(db.Text)
    dob = db.Column(db.DateTime, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return f'User({self.id}, {self.email}, {self.first_name})'

    @property
    def password(self):
        raise AttributeError('Unreadable property password.')

    @password.setter
    def password(self, password):
        if password:
            self._password_hash = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()
            ).decode()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self._password_hash.encode())
    
    def __hash__(self) -> int:
        return self.id
    
    def __eq__(self, other) -> bool:
        return self.id == other.id

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'address': self.address,
            'dob': datetime.strftime(self.dob, '%Y-%m-%d'),
        }

    def parents(self) -> Set['User']:
        from database.models import Parent
        all_parents = (
            User.query
            .join(Parent, Parent.parent_id == User.id)
            .filter(Parent.child_id == self.id)
            .all()
        )
        return all_parents

    def children(self):
        from database.models import Parent
        children = (
            User.query
            .join(Parent, Parent.child_id == User.id)
            .filter(Parent.parent_id == self.id)
            .all()
        )
        return children

    def children_recursive(self):
        """Get children of this user recursively."""
        children = set()
        for child in self.children():
            children.add(child)
            children.update(child.children_recursive())
        return children

    def siblings(self):
        from database.models import Sibling
        
        siblings_from_db_1 = (
            User.query
            .join(Sibling, Sibling.sibling_id == User.id)
            .filter(Sibling.user_id == self.id)
            .all()
        )
        siblings_from_db_2 = (
            User.query
            .join(Sibling, Sibling.user_id == User.id)
            .filter(Sibling.sibling_id == self.id)
            .all()
        )

        siblings = set(siblings_from_db_1) | set(siblings_from_db_2)
        for parent in self.parents():
            siblings.update(parent.children())

        return siblings - {self}

    def grandparents(self):
        grandparents = set()
        for parent in self.parents():
            grandparents.update(parent.parents())
        return grandparents
