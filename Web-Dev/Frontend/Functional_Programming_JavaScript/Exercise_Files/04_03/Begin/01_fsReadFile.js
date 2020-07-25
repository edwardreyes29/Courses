// Learning Functional Programming with Javascript
// Chapter 04, Video 03, Exercise 01
var fs = require('fs')

var fileContents

// Asynchronous
fs.readFile('message.txt', 'utf8', function(err, data) {
  if (err) throw err
  console.log(data)
  fileContents = data
})

console.log(fileContents) // will be undefined
