from http_server import get_class, class_get, push_name
from Pre_operation import check_satisfy
import psycopg2 as psy

# if __name__=="__main__":
#     # push_name("student_home/student_home.html?sid=11911309&name=梁鲁降&college=赫奇帕奇(Hufflepuff)&gender=男")


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

    check=check_satisfy(encode_r,length_r, pre_list)

    if length_r==0 or check==1:
        r=True
    else:
        r=False
    return done,r

if __name__ == '__main__':
    a,b=pre('MSE330-16', "11128333")


