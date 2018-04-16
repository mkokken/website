from flask import render_template, url_for, redirect, request, flash
from flask_script import Manager
from app import app
from app.forms import LoginForm, CalculateForm, TestForm, InputForm
import numpy as np
import sys
from nvd3 import pieChart, lineWithFocusChart
import random 
import datetime 
import time 
from graphs import create_pie_chart, create_line_chart, create_area_chart, create_line_chart2




@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index2', methods=['GET','POST'])
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
        test_array = np.random.randn(1,int(henk))
        jan = np.cos(float(henk))
        string = "De beste groene investering is " + str(jan) 
        
        print(henk)
        print(tmp)
        result_pie_chart = create_pie_chart(int(E), int(tmp))
        result_line_chart = create_line_chart(int(henk), int(tmp))
#        result_area_chart = create_area_chart()
#        result_line_chart2 = create_line_chart2(int(tmp))


           
    return render_template('index2.html', title='Analyse',form=form, jan=jan, string=string, test_array=test_array, result_pie_chart=result_pie_chart, E=E, result_line_chart=result_line_chart)

@app.route('/testfile')
def testfile():
    form = TestForm()
    return render_template('testfile.html', title='Test', form=form)
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