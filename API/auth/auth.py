from database.models import User


def authenticate(email, password):
    user = User.get_by(email=email)
    if user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.get(pk=user_id)
