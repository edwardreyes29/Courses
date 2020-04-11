const fs = require("fs");
/* Don't need fs to read json documents, can require directly */
const colorData = require("./assets/colors.json");

colorData.colorList.forEach(c => {
    /* Will create new file if file doesn't exist.
        Will append to it if it does.
    */
    fs.appendFile("./storage-files/colors.md", `${c.color}: ${c.hex} \n`, err => {
        if (err) {
            throw err;
        }
    }); 
});