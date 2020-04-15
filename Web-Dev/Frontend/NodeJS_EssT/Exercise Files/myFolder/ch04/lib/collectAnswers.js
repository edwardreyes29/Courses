const readline = require("readline");
const { EventEmitter } = require("events");

// Takes in input, sends output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


/* Collect  to ask every questions in array and present it to user.
    The callback should list the answers back.

    f => f dummy function, just returns args sent to it. Won't
    break code. Makes call back optional.
*/
module.exports = (questions, done = f => f) => {
    const answers = [];
    const [firstQuestion] = questions; // destructure array
    const emitter = new EventEmitter();
    
    // arguments is an array answer
    const questionAnswered = answer => {
        emitter.emit("answer", answer); // raise an event everytime a user enters an answer.
        answers.push(answer);
        // ask another question if answer length is less than questions length
        if (answers.length < questions.length) {
            rl.question(questions[answers.length],questionAnswered); // 1 -> second question, 2 -> third
        } else {
            emitter.emit("complete", answers); // listen for complete events
            // done(answers); // callback function
        }
    };

    rl.question(firstQuestion, questionAnswered);

    return emitter;
};
