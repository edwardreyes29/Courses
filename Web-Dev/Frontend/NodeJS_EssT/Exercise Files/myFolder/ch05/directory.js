const fs = require("fs");

fs.mkdir("storage-files", err => {
    /* If directory already exist, will cause an error */
    if (fs.existsSync("storage-files")) {
        console.log("Directory already exists");
    } else {
        if (err) { 
            throw err;
        }
    
        console.log("directory created");
    }
});