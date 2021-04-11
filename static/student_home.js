

window.onload=function () {
    console.log("start")
    var sid = Utils.getRequest(sid);
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
        "<td>名称</td>"+
        "<td>学分</td>"+
        "<td>部门</td>");
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
                    t_classes.insertAdjacentHTML("afterend", "<th>"+arr.course_id+"</th>" +
                        "<td>"+arr.course_name+"</td>"+
                        "<td>"+arr.course_credit+"</td>"+
                        "<td>"+arr.course_dept+"</td>"
                    );

                }
                // t_classes.innerHTML="<th>课程:</th>\n" +
                //     "            <td ></td>\n" +
                //     "            <th>简称:</th>\n" +
                //     "            <td ></td>";

            }
        }
    );

}
