

window.onload=function () {
    console.log("start")
    var sid = Utils.getRequest().sid;
    var t_sid=document.getElementById("sid");
    var t_name=document.getElementById("name");
    var t_college=document.getElementById("college");
    var t_profile=document.getElementById("gender");
    var t_classes=document.getElementById("class");

    var param=Utils.getRequest();

    t_sid.innerText=param['sid'];
    t_name.innerText=param['name'];
    t_college.innerText=param['college'];
    t_profile.innerText=param['gender'];

    t_classes.insertAdjacentHTML("afterbegin","<th>已修课id</th>" +
        "<th>名称</th>"+
        "<th>学分</th>"+
        "<th>部门</th>");
    $.ajax(
        {
            url:Utils.server+"class_get",
            type:'get',
            dataType:'jsonp',
            jsonpCallback:'class_get',
            data:{
                sid:param['sid']
            },
            complete:function (data,textStatus){
                console.log(data);
            },
            success:function (data,textStatus){
                console.log("Success");
                console.log(data);

                for (var arr of data) {
                    t_classes.insertAdjacentHTML("afterend", "<td>"+arr.course_id+"</td>" +
                        "<td>"+arr.course_name+"</td>"+
                        "<td>"+arr.course_credit+"</td>"+
                        "<td>"+arr.course_dept+"</td>"
                    );

                }

            }
        }
    );

}

function query() {
    var sid = Utils.getRequest().sid;
    console.log(sid);
    var course_id=document.getElementById("course_id").value;
    var hint=document.getElementById('hint');
    if(course_id.length===0){
        hint.innerText='请输入课程信息哦!';
    }
    $.ajax(
        {
            url:Utils.server+"pre_course_query",
            type: 'get',
            dataType: 'jsonp',
            jsonpCallback: 'pre_course_query',
            data: {
                's_sid':sid,
                'course_id':course_id
            },
            success:function (data,textStatus) {
                console.log('success')
                console.log(data);
                var show_classes=document.getElementById('class_qualified');
                var pres=document.getElementById("pres");
                var result=document.getElementById("result");
                if(data.list.length===0){
                    hint.innerText='查无此课';
                }else{
                    pres.innerText="需要上这门课,你需要预先学习:"+data.pres;
                    show_classes.innerText="要上这门课,你已经修过的魔法有:"+data.list+"\n";
                    str="所以,你"+data.qualified?"":"不"+"能上这门课";
                    result.innerText= str;

                }
            }

        }
    )
}
