// commonjs module pattern: require and exports
const path = require("path"); // get the path module
console.log(`The full file path is ${path.dirname(__filename)}`);
console.log(`The file name is ${path.basename(__filename)}`); // The file name is global.js

console.log(__dirname); // returns full path to directory
console.log(__filename);    // returns full path to file