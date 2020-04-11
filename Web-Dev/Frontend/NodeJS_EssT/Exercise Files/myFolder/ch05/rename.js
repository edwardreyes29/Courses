const fs = require("fs");

fs.renameSync("./assets/colors.json", "./assets/colorData.json");

/* can use rename to move files as well */
fs.rename("./assets/notes.md", "./storage-files/notes.md", err => {
    if (err) {
        throw err;
    }
});

setTimeout(() => {
    fs.unlinkSync("./assets/alex.jpg"); // delete file
}, 4000)