var stripThis = "https://www.youtube.com/watch?v=";

chrome.tabs.query({active: true, lastFocusedWindow: true}, function(tabs) {
    var currentUrl = tabs[0].url;
    var smallUrl = currentUrl.substring(stripThis.length, currentUrl.length);
    //alert(smallUrl)//just to check
    document.getElementById("demo").innerHTML=smallUrl;
    document.getElementById("t1").value=smallUrl;

    
    //var pathDL = "URLs/"+smallUrl+".txt"; not use    
});

var py_data=document.getElementById("data").innerHTML;
document.getElementById("sumry").innerHTML=py_data;
document.getElementById("sumry").value=py_data;

/*
function myFunction()
        {
        var vid=document.getElementById("demo").innerHTML;
        alert(vid);
        localStorage.setItem("para",vid);
        }*/

