console.log("hello");

function btn(index){
    switch (index) {
        case 0://student
            window.open("student_login.html");
            // window.location.replace("../student_login/student_login.html");
            break;
        case 1://admin
            window.open("admin_login.html");
            break;
        default:
            window.alert("麻瓜不可登录!");
            break;
    }
}
