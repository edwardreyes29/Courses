/* Stream interface, read and write data files, processes, internet, terminal */

const fs = require("fs");

const readStream = fs.createReadStream("./assets/lorum-ipsum.md", "UTF-8");

let fileTxt = "";

/* Reading files with steam uses less memory. The text file is being read bit by bit (chunk by chunk) 
  Doesn't read everything at once and loads them into a buffer.
*/
console.log("type something...");
readStream.on("data", data => {
  console.log(`I read ${data.length - 1} characters of text`);
  fileTxt += data;
});

readStream.once("data", data => {
  console.log(data);
});

/* end event */
readStream.on("end", () => {
  console.log("finished reading a file");
  console.log(`In total I read ${fileTxt.length - 1} characters of text`);
});