const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const questions = [
    "What is your name? ",
    "Where do you live? ",
    "What are you going to do with node js? "
];

/* Collect  to ask every questions in array and present it to user.
    The callback should list the answers back.
*/

const collectAnswers = (questions, done) => {
    const answers = [];
    const [firstQuestion] = questions; // destructure array
    
    const questionAnswered = answer => {
        answers.push(answer);
        // ask another question if answer length is less than questions length
        if (answers.length < questions.length) {
            rl.question(questions[answers.length],questionAnswered); // 1 -> second question, 2 -> third
        } else {
            done(answers); // callback
        }
    };

    rl.question(firstQuestion, questionAnswered);
};

collectAnswers(questions, answers => {
    console.log("Thank you for your answers. ");
    console.log(answers);
    process.exit();
});

