# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:35:09 2021

@author: 11911627 Tan Sixu
"""
import json

from flask import Flask, render_template
from flask import escape, url_for, request, jsonify
from funct import get_class, info, pre, insert_ss, insert_course, insert_teacher
import psycopg2 as psy

app = Flask(__name__)


@app.route('/')
def hello():
    print('Start to serve you, my lord')
    return render_template('First.html')


@app.route('/<name>')
def push_name(name):
    # nnammee='%s' % escape(name)
    # index = nnammee.split('/')
    # names=index[-1]
    if name=="favicon.ico":
        with open('templates/favicon.ico','rb') as f:
            return f.read()

    return render_template(name)
    # return 'user: %s' % escape(name)


@app.route('/student_login/', methods=['GET', 'POST'])
def student_login():
    print("value:")
    sid = request.args.get('sid')
    tt = info(sid)
    if len(tt)==0:
        data={
            "sid":-1
        }
        tt=json.dumps(data)
        tt = "%s(%s)" % ('student_login', tt)
        print(tt)
        return tt
        pass
    data = {
        "sid": sid,
        "name": tt[0][0],
        "gender": tt[0][1],
        "college": tt[0][2]
    }
    tt = json.dumps(data)
    tt = "%s(%s)" % ('student_login', tt)
    print(tt)
    return tt


@app.route('/class_get/', methods=['GET', 'POST'])
def class_get():
    print("value:")
    # sid = '11911309'
    sid = request.args.get('sid')
    data=get_class(sid)
    tt = json.dumps(data)
    tt = "%s(%s)" % ('class_get', tt)
    print(tt)
    return tt


@app.route('/admin_login/', methods=['GET', 'POST'])
def admin_login():
    pass

@app.route('/pre_course_query/', methods=['GET','POST'])
def check_pre():
    cid=request.args.get('course_id')
    sid=request.args.get('s_sid')
    con=pre(cid,sid)
    print(con)
    return con


@app.route('/admin_add_student/', methods=['GET', 'POST'])
def add_ss():
    print("start to add student")
    name=request.args.get('name')
    sid=request.args.get('sid')
    gender=request.args.get('gender')
    college=request.args.get("college")
    course_raw=request.args.get("pres")
    course=course_raw.split(',')
    con=insert_ss(name, gender, college, sid, course)
    print(con)
    return con


@app.route('/admin_add_course/',methods=['GET', 'POST'])
def add_course():
    print("start to add course")
    cid=request.args.get("course_id")
    c_name=request.args.get("course_name")
    tot_cap=int(request.args.get("total_capacity"))
    c_hour=int(request.args.get("course_hour"))
    c_dept=request.args.get("course_dept")
    c_credit=float(request.args.get("course_credit"))
    pres=request.args.get("pres")
    con=insert_course(cid, c_name,tot_cap,c_hour,c_dept,c_credit, pres)
    print(con)
    return con

@app.route('/admin_add_teacher/', methods=['GET', 'POST'])
def add_teacher():
    print("start to add teacher")
    name=request.args.get("name")
    con=insert_teacher(name)
    return con

if __name__ == '__main__':
    app.run('10.17.118.214', 8000)



