from database import db
from database.models import User
from database.models._crud import CRUDMixin


class Parent(CRUDMixin, db.Model):
    __tablename__ = 'parents'
    __table_args__ = (
        db.UniqueConstraint('child_id', 'parent_id', name='_child_parent_uc'),
    )

    id = db.Column(db.Integer, primary_key=True)

    child_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    parent_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Parent({self.child()} -> {self.parent()})'

    def child(self) -> User:
        return User.get(self.child_id)

    def parent(self) -> User:
        return User.get(self.parent_id)
