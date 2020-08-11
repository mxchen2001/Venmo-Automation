/** upload.js */
const electron = require('electron'); 
const path = require('path'); 
const fs = require('fs');


// Importing dialog module using remote 
const dialog = electron.remote.dialog; 
  
var uploadFile = document.getElementById('uploadToVenmo'); 
  
// Defining a Global file path Variable to store user-selected file 
global.filepath = path.join(__dirname); 
  
uploadFile.addEventListener('click', () => { 
// If the platform is 'win32' or 'Linux' 
        if (process.platform !== 'darwin') { 
            // Resolves to a Promise<Object> 
            dialog.showOpenDialog({ 
                title: 'Select the File to be uploaded', 
                defaultPath: path.join(__dirname, '../assets/'), 
                buttonLabel: 'Upload', 
                // Restricting the user to only Text Files. 
                filters: [ 
                    { 
                        name: 'Text Files', 
                        extensions: ['xlsx'] 
                    }, ], 
                // Specifying the File Selector Property 
                properties: ['openFile']
        }).then(file => { 
          console.log(file.canceled); 
          var upload_file_name;
          var upload_file_extension;
          if (!file.canceled) { 
            global.filepath = file.filePaths[0].toString(); 
            upload_file_name = global.filepath.toString().split('\\').pop().split('/').pop();
            upload_file_extension = global.filepath.toString().split('.').pop();
            console.log('Uploaded File: ' + upload_file_name);
            console.log('File Type: ' + upload_file_extension);
            console.log('Global filepath: ' + global.filepath); 
          }   
          if (global.filepath && !file.canceled) { 

            fs.readFile(global.filepath, (err, data) => {
              if (!err) { 
                console.log('received data: ' + data); 
                console.log(global.filepath);
                var upload_file_path = path.join(__dirname, '../../assets/static/input.xlsx');
                fs.writeFileSync(upload_file_path, data, 'binary');
                var el = document.getElementById("consoleOut");
                var currentEl = "<p style='padding-left: 20px;'>Your file: <a target='_blank' rel='noopener noreferrer' href="+ global.filepath +">" + upload_file_name + "</a></p>";
                el.innerHTML = currentEl;
                document.getElementById("consoleOut").innerHTML = el.innerHTML;
              } else { 
                  console.log(err); 
              }
            });
          }
        }).catch(err => { 
            console.log(err) 
        }); 
    } else { 
        // If the platform is 'darwin' (macOS) 
        dialog.showOpenDialog({ 
            title: 'Select the File to be uploaded', 
            defaultPath: path.join(__dirname), 
            buttonLabel: 'Upload', 
            filters: [ 
                { 
                    name: 'Spreadsheet', 
                    extensions: ['xlsx'] 
                }, ], 
            // Specifying the File Selector and Directory Selector Property In macOS 
            properties: ['openFile', 'openDirectory'] 
        }).then(file => { 
            console.log(file.canceled); 
            var upload_file_name;
            var upload_file_extension;
            if (!file.canceled) { 
              global.filepath = file.filePaths[0].toString(); 
              upload_file_name = global.filepath.toString().split('\\').pop().split('/').pop();
              upload_file_extension = global.filepath.toString().split('.').pop();
              console.log('Uploaded File: ' + upload_file_name);
              console.log('File Type: ' + upload_file_extension);
              console.log('Global filepath: ' + global.filepath); 
            }   
            if (global.filepath && !file.canceled) { 

              fs.readFile(global.filepath, (err, data) => {
                if (!err) { 
                  console.log('received data: ' + data); 
                  console.log(global.filepath);
                  var upload_file_path = path.join(__dirname, '../../assets/static/input.xlsx');
                  fs.writeFileSync(upload_file_path, data, 'binary'); 

                  var el = document.getElementById("consoleOut");
                  var currentEl = "<p style='padding-left: 20px;'>Your file: <a target='_blank' rel='noopener noreferrer' href="+ global.filepath +">" + upload_file_name + "</a></p>";
                  el.innerHTML = currentEl;
                  document.getElementById("consoleOut").innerHTML = el.innerHTML;
                } else { 
                    console.log(err); 
                }
              });
            }
        }).catch(err => { 
            console.log(err) 
        }); 
    } 
}); 