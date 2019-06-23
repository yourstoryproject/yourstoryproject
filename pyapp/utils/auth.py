from flask import redirect, url_for
from flask_login import current_user
from functools import wraps


def role_required(role):
    def decorator(func):
        @wraps(func)
        def authorize(*args, **kwargs):
            if not current_user.has_role(role):
                return redirect(url_for('auth'))
            return func(*args, **kwargs)

        return authorize

    return decorator
