from database.models import User


def authenticate(email, password):
    user = User.get_by(email=email)
    if user.check_password(password):
        return user


def identity(payload):
    print('*' * 100)
    print(payload)
    user_id = payload['identity']
    print(user_id)
    return User.get(pk=user_id)
