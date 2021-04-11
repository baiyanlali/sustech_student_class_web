
var tab_list;
function changeTab(num){
    if(tab_list===undefined){
        tab_list=new Array();
        tab_list[0]=document.getElementById("add_student");
        tab_list[1]=document.getElementById("add_course");
        tab_list[2]=document.getElementById("add_teacher");
        tab_list[3]=document.getElementById("quote_course");

    }
    for (let i = 0; i < tab_list.length; i++) {
            tab_list[i].className = "";
    }
    tab_list[num].className="active";
    console.log(num)
}