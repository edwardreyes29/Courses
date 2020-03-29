console.log(process.pid);
console.log(process.versions.node);
/*
    returns an array of everything we typed to run the process.
    First process was running node, so it shows the path for node. (node)
    Second process is running globalProcess.js, so it shows the path for that process. (current module being used)
*/
console.log(process.argv);

// Array destructuring

// const [,,firstName, lastName] = process.argv;

// console.log(`Your name is ${firstName} ${lastName}`);

// node globalProcess Edward Reyes -> the array elements will be sent to the variables firstName and lastName
// This allows us to send arguments to nodejs module when we run it.

/*
    node globalProcess flags to tell what kind of variables the node module will be passed

    node globalProcess --user ned --greeting "Winter is coming."

*/

// The grab function will find the index of --greeting or --user and return the next index
const grab = flag => {
    let indexAfterFlag = process.argv.indexOf(flag) + 1;
    return process.argv[indexAfterFlag];
};

const greeting = grab("--greeting");
const user = grab("--user");

console.log(`${greeting} ${user}`);