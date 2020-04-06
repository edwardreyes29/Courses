const path = require("path"); // require core (came with nodejs) node module
const util = require("util");
const { log } = require("util"); // destructure, can get specific functions
const v8 = require("v8");

// Path module
const dirUploads = path.join(__dirname, 'www','files','uploads');
console.log(dirUploads);
// const base = path.basename(dirUploads);
// console.log(`Base name: ${base}`);

// Utilities module
util.log( path.basename(__filename) ); // like console log, but includes date and time stamp
util.log(" ^ The name of the current file");

// v8 modules
log(v8.getHeapStatistics());

