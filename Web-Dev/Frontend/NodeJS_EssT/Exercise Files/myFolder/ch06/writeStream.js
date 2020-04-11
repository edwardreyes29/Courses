const fs = require("fs");

const writeStream = fs.createWriteStream("./assets/myFile.txt", "UTF-8");
const readStream = fs.createReadStream("./assets/lorum-ipsum.md", "UTF-8");

// process.stdout.write("hello");
// process.stdout.write(" world\n");

/* Write output to a file */
// writeStream.write("hello");
// writeStream.write(" world\n");


/* Readable streams are made to work with writable streams */
// process.stdin.on("data", data => {
//     writeStream.write(data);
// });

/* Copies lorum-ipsum contents to myFile */
// readStream.on("data", data => {
//     writeStream.write(data); 
// });

// process.stdin.pipe(writeStream);
readStream.pipe(writeStream);