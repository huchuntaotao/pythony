#! /usr/bin/env python
# -*- coding: utf-8 -*-

from . import main
from forms import NameForm
from flask import redirect, url_for,render_template,session,current_app
from datetime import datetime
from ..models import User
from .. import db
from ..email import send_email

@main.route('/mail/', methods=['GET','POST'])
def mail():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if current_app.config['PYTHONY_ADMIN']:
                send_email(current_app.config['PYTHONY_ADMIN'], 'NEW_USER', '/mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.mail'))
    return render_template('mail/index.html', form=form, 
                           name = session.get('name'),
                           known=session.get('known', False), 
                           current_time=datetime.utcnow())
    
@main.route('/')
def index():
    return render_template('index.html')