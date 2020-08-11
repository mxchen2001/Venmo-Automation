const fs = require('fs');
const { spawn } = require('child_process');
const python = spawn('python', ['desktop_app/python/clear_session.py']);
python.stdout.on('data', function (result) {
    console.log('Clearing Previous Inputs');
});
python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
});


try {
    var upload_file_path = __dirname + '/../../access_token.txt';
    fs.readFile(upload_file_path, {encoding: 'utf-8'}, function(err,data) { 
        if (!err) { 
            console.log(data)
            var loginStatus;
            const python = spawn('python', ['desktop_app/python/validate_access_token.py']);
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
                }
            });
        } else { 
            console.log(err); 
        } 
    }); 
}
catch(err) {
    console.log(err); 
}
