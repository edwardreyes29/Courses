const waitTime = 5000; // 3000 ms = 3 sec
const waitInterval = 500; // half second
let currentTime = 0; // want to change so declare as let

const incTime = () => {
    currentTime += waitInterval;
    const p = Math.floor((currentTime/waitTime) * 100);
    process.stdout.clearLine(); // clears last line
    process.stdout.cursorTo(0); // start of the line
    process.stdout.write(`waiting ... ${p}%`)
}

console.log(`setting a ${waitTime / 1000} second delay`);

const timerFinished = () => {
    clearInterval(interval);
    process.stdout.clearLine(); // clears last line
    process.stdout.cursorTo(0); // start of the line
    console.log("done");
}

const interval = setInterval(incTime, waitInterval); // gets called every half seccond
setTimeout(timerFinished, waitTime);