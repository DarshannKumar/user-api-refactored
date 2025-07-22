def validate_user_data(data):
    if not data.get('name'):
        return "Name is required"
    if not data.get('email'):
        return "Email is required"
    if not data.get('password'):
        return "Password is required"
    return None


def validate_login_data(data):
    if not data.get('email'):
        return "Email is required"
    if not data.get('password'):
        return "Password is required"
    return None
