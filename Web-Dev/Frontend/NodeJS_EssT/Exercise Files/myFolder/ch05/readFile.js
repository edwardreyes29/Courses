/* FS module to read contents of a file */
const fs = require("fs");

// const text = fs.readFileSync("./assets/Readme.md", "UTF-8");

/* Reading binary files doesn't require encoding arg */
fs.readFile("./assets/alex.jpeg", (err, img) => {
    if (err) {
        console.log(`An error has occurred: ${err.message}`);
        process.exit();
    }
    console.log(img);
});

// console.log(text);