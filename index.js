// const express = require('express')
// const {spawn} = require('child_process');
// const app = express()
// const port = 3000
// app.get('/', (req, res) => {
 
//  var dataToSend;
//  // spawn new child process to call the python script
//  const python = spawn('python', ['js_python_test.py','node.js','python']);
//  // collect data from script
//  python.stdout.on('data', function (data) {
//   console.log('Pipe data from python script ...');
//   dataToSend = data.toString();
//  });
//  // in close event we are sure that stream from child process is closed
//  python.on('close', (code) => {
//  console.log(`child process close all stdio with code ${code}`);
//  // send data to browser
//  res.send(dataToSend)
//  });
 
// })
// app.listen(port, () => console.log(`Example app listening on port 
// ${port}!`))


const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {
var largeDataSet = [];
 // spawn new child process to call the python script
 const python = spawn('python', ['js_python_test.py']);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  largeDataSet.push(data);
 });
 // in close event we are sure that stream is from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(largeDataSet.join(""))
 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))