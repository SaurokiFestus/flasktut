from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required #cannot get to the homepage without logging in
def home():
    if request.method =='POST':
        note = request.form.get('note')

        if not note:
            flash('Note cannot be empty', category='error')
        elif len(note)<= 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(text=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added', category='success')
    return render_template("home.html", user=current_user)
    