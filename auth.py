from database import add_user, validate_user

def register_user(username, password):
    add_user(username, password)

def login_user(username, password):
    return validate_user(username, password)