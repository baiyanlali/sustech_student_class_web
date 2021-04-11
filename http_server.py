# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:35:09 2021

@author: 11911627 Tan Sixu
"""
import json

from flask import Flask, render_template
from flask import escape, url_for, request, jsonify
import psycopg2 as psy


def info(sid):
    db = psy.connect(database='CS307_SustechStudentClass', user='byll', password='123456', host='10.17.118.214',
                     port='5432')
    cur = db.cursor()
    cur.execute("set search_path = 'Public'")
    cur.execute("""select name,case gender when 'F' then '女' when 'M' then '男' end as gender, college
                from student s
                where s.student_id='%s'
                """ % sid)
    rows1 = cur.fetchall()

    return rows1


def get_class(sid):
    db = psy.connect(database='CS307_SustechStudentClass', user='byll', password='123456', host='10.17.118.214',
                     port='5432')
    cur = db.cursor()
    cur.execute("set search_path = 'Public'")

    cur.execute("""select course_id,c.coursename,c.coursecredit,c.coursedept
                from coursedone
                left join course c on c.courseid=course_id
                where student_id='%s'
                """ % sid)
    rows = cur.fetchall()

    data_con=[]
    for row in rows:

        data={
            "course_id":row[0],
            "course_name":row[1],
            "course_credit":row[2],
            "course_dept":row[3]
        }
        data_con.append(data)
    return data_con


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


if __name__ == '__main__':
    app.run('10.17.118.214', 8000)


