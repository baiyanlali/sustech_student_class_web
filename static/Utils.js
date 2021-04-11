var Utils={
    server:"http://10.17.118.214:8000/",
    getRequest:function () {

        var url=window.location.search;
        url=decodeURI(url)
        if(url.indexOf("?")!==-1){
            var con=new Object();
            var str=url.substr(1);
            var strr=str.split('&');
            for (const string of strr) {
                var params=string.split("=");
                con[params[0]]=params[1];
                // console.log("pa0:"+params[0]+"\npa1:"+params[1]);
            }
            return con;
        }
    }
}


