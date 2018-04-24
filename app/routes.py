from flask import render_template, url_for, redirect, request, flash
from flask_script import Manager
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, CalculateForm, TestForm, InputForm, RegistrationForm
import numpy as np
import time 
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User

from graphs import create_pie_chart, create_line_chart, create_area_chart, create_line_chart2




@app.route('/')
@app.route('/index')
#@login_required
def index():
    user = {'username': 'Mitchel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index2', methods=['GET','POST'])
@login_required
def index2():
    jan = ''
    henk = ''
    string = ''
    test_array = ''
    result_pie_chart = ''
    result_area_chart = ''
    result_line_chart = ''
    result_line_chart2 = '' 
    E = ''
    form = CalculateForm()
    if form.validate_on_submit():

        henk = form.area.data
        tmp = form.jaar.data
        E = form.energieverbruik.data
        jan = np.cos(float(henk))
        string = "De beste groene investering is " + str(jan)
        start = time.clock()
        result_pie_chart = create_pie_chart(int(E), int(tmp))
        tijd = start - time.clock()
        print(tijd)
        start = time.clock()
        result_line_chart = create_line_chart(int(tmp))
        tijd = start - time.clock()
        print(tijd)
#        result_area_chart = create_area_chart()
#        result_line_chart2 = create_line_chart2(int(tmp))


           
    return render_template('index2.html', title='Analyse',form=form, jan=jan, string=string, test_array=test_array, result_pie_chart=result_pie_chart, E=E, result_line_chart=result_line_chart)


@app.route('/registreer')
#@login_required
def registreer():
    form = TestForm()
    return render_template('registreer.html', title='Test', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/testfile')
@login_required
def testfile():

    form = TestForm()
    return render_template('registreer.html', title='Test', form=form)
#
#@app.route('/graph') 
#def plotpage(): 
#    type = 'pieChart'
#    chart = pieChart(name=type, color_category='category20c', height=450, width=450)
#    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
#    ydata = [3, 4, 0, 1, 5, 7, 3]
#    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
#    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
#    chart.buildhtml()
#    result = chart.htmlcontent
#
#    return render_template('graph.html', result=result) 
#        