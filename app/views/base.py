from flask import Blueprint, render_template, session, redirect, url_for, flash, request, current_app

from app.forms.login import LoginForm
from app.helpers.login import login_required
from app.models.models import User
from app.utils.bcrypt import bcrypt

base_bp = Blueprint('base', __name__)


@base_bp.route('/')
@login_required
def main():

    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['USERS_PER_PAGE']

    user = User.query.filter_by(user_id=session['user_id']).first()
    users = User.query.filter(User.role != 'admin')

    users_pag = users.paginate(page=page, per_page=per_page)

    users_length = len(users.all())

    return render_template('main.html', users=users_pag, user=user, users_length=users_length)


@base_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                session['user_id'] = user.user_id
                return redirect(url_for('base.main'))

        flash('The username or password is incorrect')

    return render_template('login.html', form=form)


@base_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', 1, type=str)

    user = User.query.filter_by(user_id=session['user_id']).first()

    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['USERS_PER_PAGE']

    results = User.query.filter(
        User.name.ilike(f'%{query}%') | User.role.ilike(f'%{query}%') | User.contact.ilike(f'%{query}%')).filter(User.role != 'admin')
    users_pag = results.paginate(page=page, per_page=per_page)

    result_length = len(users_pag.items)

    return render_template('main.html', users=users_pag, user=user, query=query, result_length=result_length)
