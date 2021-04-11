import json

import psycopg2 as psy
from Pre_operation import check_satisfy, encode, get_course_name
from flask import json
import re
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


def pre(cid, sid):
    db = psy.connect(database='CS307_SustechStudentClass', user='byll', password='123456', host='10.17.118.214',
                     port='5432')
    cur = db.cursor()
    cur.execute("set search_path = 'Public'")

    # get pre list and done
    cur.execute("""select p.standard_name, p.num
        from
        (select standard_name, num
        from pre_std_name
        where host_courseid='%s')p
        join (select c.standard_name
            from coursedone
            join course c
            on c.courseid=coursedone.course_id
            where coursedone.student_id='%s')q
        on p.standard_name=q.standard_name; """ % (cid, sid))
    rows = cur.fetchall()
    done = []
    pre_list = []
    for i, j in rows:
        done.append(i)
        pre_list.append(j)

    # get encode
    cur.execute("""select encode_pattern, length
            from pre_encode
            where course_id='%s'""" % (cid))
    rows2 = cur.fetchall()
    encode_r = rows2[0][0]
    length_r = rows2[0][1]


    #get raw expression of pre
    cur.execute("""select prerequisite
                from course
                where courseid='%s'""" % (cid))
    rows3 = cur.fetchall()
    raw_pre=rows3[0][0]

    check=check_satisfy(encode_r,length_r, pre_list)

    if check==1 or length_r==0:
        reply=True
    else:
        reply=False
    t={'list':done,'qualified':reply, 'pres':raw_pre}
    t=json.dumps(t)
    tt='%s(%s)'%('pre_course_query',t)
    return tt


#admin_ad
def insert_ss(name, gender, college, sid, pres):
    db = psy.connect(database='CS307_SustechStudentClass', user='byll', password='123456', host='10.17.118.214',
                     port='5432')
    cur = db.cursor()
    cur.execute("set search_path = 'Public'")
    print("Add student:BEFORE SQL")
    try:
        cur.execute("""insert into student (name, gender, college, student_id)
        values ('%s','%s','%s', '%s') """ % (name, gender, college, sid))

        for c in pres:
            cur.execute("""insert into coursedone(student_id, course_id)
            values ('%s','%s') """ % (sid, c))
        t={'status': 'done it'}
    except :
        t={'status': 'damn it, we fail it.'}

    t = json.dumps(t)
    print("Add student:"+t)
    tt = "%s(%s)" % ("admin_add_student", t)
    return tt


#admin_add_course
def insert_course(cid, c_name, tot_cap, c_hour, c_dept, c_credit, pres):
    db = psy.connect(database='CS307_SustechStudentClass', user='byll', password='123456', host='10.17.118.214',
                     port='5432')
    cur = db.cursor()
    cur.execute("set search_path = 'Public'")

    std=re.sub(r'\(|\)|\s|（|）', "", c_name)
    print("Add course:BEFORE SQL")
    try:
        #insert course
        cur.execute("""insert into course(courseid, totalcapacity, coursename, coursehour, coursedept, coursecredit, standard_name, prerequisite)
        VALUES ('%s',%d,'%s','%s','%s',%f, '%s', '%s') """ % (cid, tot_cap, c_name, c_hour,c_dept,c_credit,std))


        #insert encode
        en_pattern, length=encode(pres)
        cur.execute("""insert into pre_encode(course_id, encode_pattern, length) 
            VALUES ('%s','%s',%d)"""%(cid, en_pattern, length))

        #insert pre_std_names
        all_pres=get_course_name(pres)
        for i in range(len(all_pres)):
            c=all_pres[i]
            cur.execute("""insert into pre_std_name(host_courseid, standard_name, num) 
                    values ('%s','%s',%d)"""%(cid, c, i))

        t={'status': 'done it'}
    except :
        t={'status': 'damn it, we fail it.'}

    t = json.dumps(t)
    print("Add student:"+t)
    tt = "%s(%s)" % ("admin_add_student", t)
    return tt