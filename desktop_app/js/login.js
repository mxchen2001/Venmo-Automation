
function venmoLogin () {
    if (document.getElementById("access_token").value != ""){
        var access_token = document.getElementById("access_token").value;
        var loginStatus;
        const { spawn } = require('child_process');
        const python = spawn('python', ['desktop_app/python/login.py', access_token]);
        python.stdout.on('data', function (result) {
            console.log('Pipe data from python script ...');
            dataToSend = result.toString();
            loginStatus = dataToSend.substring(0, 3)
            console.log("dataToSend: " + loginStatus)
        });
        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            if (loginStatus == 'Suc') {
                window.location.replace('../templates/dashboard.html');
            } else {
                document.getElementById('loginInvalid').style.display = "block";
                document.getElementById('loginEmpty').style.display = "none";
            }
        });
    } else {
        document.getElementById('loginEmpty').style.display = "block";
        document.getElementById('loginInvalid').style.display = "none";

    }
}

function venmoLogout () {
    const { spawn } = require('child_process');
    const python = spawn('python', ['desktop_app/python/logout.py']);
    python.stdout.on('data', function (result) {
        console.log('Pipe data from python script ...');
        dataToSend = result.toString();
        console.log("dataToSend: " + dataToSend)
    });
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        window.location.replace('../templates/index.html');
    });
}