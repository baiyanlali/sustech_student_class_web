# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:35:09 2021

@author: 11911627 Tan Sixu
"""
import json

from flask import Flask, render_template
from flask import escape, url_for, request, jsonify
from funct import get_class, info, pre
import psycopg2 as psy

app = Flask(__name__)


@app.route('/')
def hello():
    print('Start to serve you, my lord')
    return render_template('First.html')


@app.route('/<name>')
def push_name(name):
    nnammee='%s' % escape(name)
    index = nnammee.split('/')
    names=index[-1]
    return render_template(names)
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


if __name__ == '__main__':
    app.run('10.17.118.214', 8000)



