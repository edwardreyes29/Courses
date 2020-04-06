const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/*
    The answer will be supplied as an argument to callback function
*/
rl.question("How do you like Node? ", answer => {
    console.log(`Your answer: ${answer}`);
});