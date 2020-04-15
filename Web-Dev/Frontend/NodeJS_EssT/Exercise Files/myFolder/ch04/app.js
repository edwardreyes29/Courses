/* No module needed for core modules */

const counter = require("./myModule"); // export value of module.exports

counter.inc();
counter.inc();
counter.inc();
counter.dec();

console.log(counter.getCount());

// const {inc, dec, getCount} = require("./myModule");
// inc();
// inc();
// inc();
// inc();
// dec();
// console.log(getCount());