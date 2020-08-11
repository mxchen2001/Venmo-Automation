
function sendToVenmo() {
    const { spawn } = require('child_process');
    var printOut = "no input"
    const python = spawn('python', ['desktop_app/python/venmo_read_spreadsheet.py']);
    python.stdout.on('data', function (result) {
        console.log('Pipe data from python script ...');
        printOut = result.toString();


        console.log("printOut: " + printOut)
    });
    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        if (code != 69){
            var el = document.getElementById("consoleOut");
            var printOutHTMLSafe = printOut.split('[94m').join('')
            printOutHTMLSafe = printOutHTMLSafe.split('[93m').join('')
            printOutHTMLSafe = printOutHTMLSafe.split('[92m').join('')
            printOutHTMLSafe = printOutHTMLSafe.split('[0m').join('')
            var printOutHTMLSafeArr = printOutHTMLSafe.split('Sending Request ... Request sent')
            var currentEl = "";
            for(i = 0; i < printOutHTMLSafeArr.length - 1; i++) {
                userCount = i + 1;
                currentEl += "<p style='padding-left: 20px;'>User " + userCount + ": " + printOutHTMLSafeArr[i] + "</p>";
                currentEl += "<p style='color: #6782B4; padding-left: 20px;'>Sending Request ... Request sent</p>";
            }
            currentEl += "<p style='color: green; padding-left: 20px;'>Completed</p>";
            el.innerHTML = currentEl;
            document.getElementById("consoleOut").innerHTML = el.innerHTML;
        } else {
            var el = document.getElementById("consoleOut");
            var currentEl = "<p style='color: red; padding-left: 20px;'>Error: No File Selected</p>";
            el.innerHTML = currentEl;
            document.getElementById("consoleOut").innerHTML = el.innerHTML;
        }
    });
}

