var stripThis = "https://www.youtube.com/watch?v=";

chrome.tabs.query({active: true, lastFocusedWindow: true}, function(tabs) {
    var currentUrl = tabs[0].url;
    var smallUrl = currentUrl.substring(stripThis.length, currentUrl.length);
    //alert(smallUrl)//just to check
    document.getElementById("demo").innerHTML=smallUrl;
    //var pathDL = "URLs/"+smallUrl+".txt"; not use
    
});

