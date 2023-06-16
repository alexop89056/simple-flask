from functools import wraps
from flask import abort, session, redirect, url_for

from app.models.models import User


def login_required(func):
    @wraps(func)
    def login_check(*args, **kwargs):

        if 'user_id' in session:
            user = User.query.filter_by(user_id=session['user_id']).first()
            if user:
                result = func(*args, **kwargs)
                return result

        return redirect(url_for('base.login'))

    return login_check


def admin_required(func):
    @wraps(func)
    def admin_check(*args, **kwargs):

        if 'user_id' in session:
            user = User.query.filter_by(user_id=session['user_id']).first()
            if user.role == 'admin':
                result = func(*args, **kwargs)
                return result

        abort(404)

    return admin_check
