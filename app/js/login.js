function makeRequest(opts) {
    return new Promise(function (resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open(opts.method, opts.url);
        xhr.onload = function () {
            if (this.status >= 200 && this.status < 300) {
                resolve(xhr.response);
            } else {
                reject({
                    status: this.status,
                    statusText: xhr.statusText
                });
            }
        };
        xhr.onerror = function () {
            reject({
                status: this.status,
                statusText: xhr.statusText
            });
        };
        if (opts.headers) {
            Object.keys(opts.headers).forEach(function (key) {
                xhr.setRequestHeader(key, opts.headers[key]);
            });
        }
        var params = JSON.stringify(opts.params);
        xhr.send(params);
    })
}

function getToken () {
    makeRequest({
        method: 'POST',
        url: 'http://localhost:5000/aak_app/researcher/api/token',
        params: {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        },
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        const fs = require('fs'); // this module contains the writeFile function
        const CryptoJS = require('crypto-js');
        
        var token = JSON.parse(response).token;
        const tokenToEncode = CryptoJS.enc.Utf8.parse(token);
        const encodedToken = CryptoJS.enc.Base64.stringify(tokenToEncode); // encode as base64 string
        
        fs.writeFile('token.txt', encodedToken, (err) => { // write encrypted data to token.txt
            if (err) throw err;
        })
        window.location.href = "../templates/dashboard.html";
    },  function () {
            document.getElementById('loginSuccess').style.display = "none";
            document.getElementById('loginError').style.display = "block";
    });
}

function venmoLogin () {
    const express = require('express')
    const {spawn} = require('child_process');
    const app = express()
    const port = 3000
    app.get('/', (req, res) => {

     var dataToSend;
     // spawn new child process to call the python script
     const python = spawn('python', ['js_python_test.py','node.js','python']);
     // collect data from script
     python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...');
      dataToSend = data.toString();
     });
     // in close event we are sure that stream from child process is closed
     python.on('close', (code) => {
     console.log(`child process close all stdio with code ${code}`);
     // send data to browser
     res.send(dataToSend)
     });

    })
    app.listen(port, () => console.log(`Example app listening on port 
    ${port}!`))
}
