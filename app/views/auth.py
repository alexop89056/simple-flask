from flask import Blueprint, session, redirect, url_for, render_template, flash
from app.helpers.login import admin_required

from app.models.models import db, User

from app.forms.edit import EditForm
from app.forms.add_user import AddUserForm

from app.utils.bcrypt import bcrypt

from secrets import token_urlsafe

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/edit-user/<string:user_id>', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    form = EditForm(obj=user)
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data
        role = form.role.data
        contact = form.contact.data

        user.name = name
        user.username = username

        if password.strip() is not '':
            user.password = bcrypt.generate_password_hash(f'{password}')

        user.role = role
        user.contact = contact

        db.session.commit()

        flash('Your data has been successfully saved')
        return redirect(url_for('auth.edit_user', user_id=user.user_id))

    return render_template('edit.html', form=form, user=user)


@auth_bp.route('/delete-user/<string:user_id>', methods=['GET'])
@admin_required
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('base.main'))


@auth_bp.route('/add-user', methods=['GET', 'POST'])
@admin_required
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        user_id = token_urlsafe(16)
        name = form.name.data
        username = form.username.data
        password = form.password.data
        role = form.role.data
        contact = form.contact.data

        new_user = User(
            user_id=user_id,
            name=name,
            username=username,
            password=bcrypt.generate_password_hash(f'{password}'),
            contact=contact,
            role=role)

        db.session.add(new_user)
        db.session.commit()

        flash('New User Successfully Created')
        return redirect(url_for('auth.add_user'))
    return render_template('add.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('base.login'))
