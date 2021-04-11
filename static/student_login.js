function onSubmit() {
    var sid=document.getElementById("sid");
    var hint=document.getElementById("hint");
    if(sid.value.length!==8){
        hint.innerHTML="请输入正确8位学号!";
        return false;
    }else{
        hint.innerHTML="分院帽正在赶来...";
        // var xmlhttp=new XMLHttpRequest();
        // xmlhttp.onreadystatechange=function () {
        //     if(this.readyState==4 && this.status==200){
        //         window.alert(xmlhttp.responseText);
        //
        //     }
        // }


        $.ajax(
            {
                // url: "http://10.17.70.0:8000/student_login",
                url: Utils.server+"student_login",
                type:'get',
                dataType:'jsonp',
                jsonpCallback:'student_login',
                data:{
                  sid:sid.value
                },
                complete:function (data,textStatus){
                    console.log(data);
                    if(data.statusText!=="load")
                        hint.innerText="分院帽被伏地魔劫走了嘤嘤嘤";
                    // else
                    //     hint.innerText="霍格沃兹欢迎你!";

                },
                success:function (data,textStatus){
                    console.log("Success");
                    console.log(data);
                    if(data.sid===-1){
                        hint.innerText="查无此人!请确认是否收到伏地魔袭击";

                    }else{
                        window.open("student_home.html?sid="+data.sid+"&name="+data.name+"&college="+data.college+"&gender="+data.gender);
//                        window.open("?sid="+data.sid+"&name="+data.name+"&college="+data.college+"&gender="+data.gender);
                    }

                }
            }
        )
        // xmlhttp.open("GET","10.17.70.0:8000?sid="+sid);
        // xmlhttp.send();
        return true;
    }

}