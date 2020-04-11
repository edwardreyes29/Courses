/* Rename and remove Directories */
const fs = require("fs");

// fs.renameSync("./storage-files", "./storage"); // to rename a directory

/* remove files in ./storage directory */
fs.readdirSync("./storage").forEach(fileName => {
    fs.unlinkSync(`./storage/${fileName}`);
});

/* Directory must be empty */
fs.rmdir("./storage", err => {
    if (err) {
        throw err;
    }
    console.log("./storage directory removed");
});