
var tab_list;
function changeTab(num){
    if(tab_list===undefined){
        tab_list=new Array();
        tab_list[0]=document.getElementById("add_student");
        tab_list[1]=document.getElementById("add_course");
        tab_list[2]=document.getElementById("add_teacher");
        tab_list[3]=document.getElementById("quote_course");

    }
    tab_list[num].class="active";
    for (let i = 0; i < tab_list.length; i++) {
        if(i!==num)
            tab_list[num].class="";
    }
    console.log(num)
}