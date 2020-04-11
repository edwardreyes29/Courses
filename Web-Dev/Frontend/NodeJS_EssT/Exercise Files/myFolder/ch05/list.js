// reads files in directory
const fs = require("fs");


// const files = fs.readdirSync("./assets"); // Executes sync, line 3 is blocking
fs.readdir("./assets", (err, files) => {
    if (err) {
        throw err;
    }
    console.log("finished reading files.");
    console.log(files);
}); // Asynchronous, but doesn't set a variable. Will pass results to callback function

console.log("started reading files"); // show readdirSync is synchronous
// console.log("finished reading files.");
// console.log(files);