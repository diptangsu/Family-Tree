from database import db
from database.models import User
from database.models._crud import CRUDMixin


class Sibling(CRUDMixin, db.Model):
    __tablename__ = 'siblings'
    __table_args__ = (
        db.UniqueConstraint('user_id', 'sibling_id', name='_user_sibling_uc'),
    )

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sibling_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Sibling({self.user()} -> {self.sibling()})'

    def user(self) -> User:
        return User.get(self.user_id)

    def sibling(self) -> User:
        return User.get(self.sibling_id)
