const events = require("events");
const emitter = new events.EventEmitter();

// Wire up a handler, a funciton to handle custom events
emitter.on("customEvent", (message, user) => {
    console.log(`${user}: ${message}`);
})

// first arg: name of event
// next set of args: data passed to custom event handlers
// emitter.emit("customEvent", "Hello Word", "Computer");
// emitter.emit("customEvent", "That's pretty cool huh?", "Edward");

process.stdin.on("data", data => {
    const input = data.toString().trim();
    if (input === "exit") {
        emitter.emit("customEvent", "Goodbye!", "process");
        process.exit();
    }
    emitter.emit("customEvent", input, "terminal");
});