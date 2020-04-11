const cp = require("child_process");

/* spawn asynchronous processes 
    first arg is command, everything else is in an array
*/
const questionApp = cp.spawn("node", ["questions.js"]);

questionApp.stdin.write("Edward \n");
questionApp.stdin.write("Burbank \n");
questionApp.stdin.write("Create Awesome Apps \n");

/* Use Standard output to terminal, handle with this callback function */
questionApp.stdout.on("data", data => {
    console.log(`from the question app: ${data}`);
});

/* close event */
questionApp.on("close", () => {
    console.log(`questionApp process exited`);
});

/* Next Steps
    Advanced Node.js -> Alex Banks 
    Advanced Node.js: Scaling Applications
    Node.js: Design Patterns
*/