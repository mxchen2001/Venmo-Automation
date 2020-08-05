window.onload = function() { // loads content when the page is refreshed
    loadContent();
}

// get description
function loadContent () {
    const fs = require('fs');
    const CryptoJS = require('crypto-js');

    var token = fs.readFileSync('token.txt', 'utf8');
    token = CryptoJS.enc.Base64.parse(token); // parse base64 token
    token = CryptoJS.enc.Utf8.stringify(token); // decode into utf8 text

    var http = new XMLHttpRequest();
    var url = 'http://localhost:5000/aak_app/researcher/api/information'
    http.open("POST", url);
    http.setRequestHeader("Content-Type", "application/json");
    http.send(JSON.stringify({token:token}));
    http.onreadystatechange = readContent;

    function readContent () { // grabs all content using website API
        if (http.readyState == 4 && http.status == 200) {
            var response = JSON.parse(http.responseText);
            
            try {
                document.getElementById("name").innerHTML = response.name;
                document.getElementById("lab").innerHTML = response.lab + " Lab";
                document.getElementById("description").innerHTML = response.description;
                document.getElementById("keywords").innerHTML = response.keywords;
                document.getElementById("website").innerHTML = response.website;
                document.getElementById("website").href = response.website;
            } catch (error) {
                console.log("There is a field that doesn't have a corresponding HTML ID");
            }
        }
    }
}
