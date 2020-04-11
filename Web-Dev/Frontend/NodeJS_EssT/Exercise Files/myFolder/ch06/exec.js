/* child process module 

    Allows you to execute external processes in you environment.
    Your Nodejs app can run and communicate with other applications
    within environment hosted.
*/

const cp = require("child_process"); // All commands are synchronous

cp.exec("open http://www.linkedin.com/learning"); // exec for synchronous commands | open a link
cp.exec("open -a Terminal ."); // opens another instance of the terminal

cp.exec("ls", (err, data, stderr) => { // execute an ls
    if (stderr) {
        console.log(stderr); // shows error from terminal and not nodejs err
    } else if (err) {
        throw err;
    }
    console.log(data);
});

/* can run node readStream.js from this directory */
cp.exec("node readStream", (err, data, stderr) => {
    console.log(data); // can see data returned from that process
});