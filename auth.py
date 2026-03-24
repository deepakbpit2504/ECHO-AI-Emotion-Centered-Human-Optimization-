from database import add_user, validate_user

def register_user(username, password):
    """
    Registers a new user
    """
    add_user(username, password)
    return True

def login_user(username, password):
    """
    Validates user login
    """
    return validate_user(username, password)