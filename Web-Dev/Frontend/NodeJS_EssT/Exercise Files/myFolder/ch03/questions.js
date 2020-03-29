// process.stdout.write("Hello ");
// process.stdout.write("World\n\n\n"); // doesn't print new line


const questions = [
    "What is your name?",
    "What would you rather be doing?",
    "What is your preferred programming language?"
];

const ask = (i=0) => {
    process.stdout.write(`\n\n\n ${questions[i]}`);
    process.stdout.write(` > `);
};

ask();

const answers = [];
process.stdin.on('data', data => {
    answers.push(data.toString().trim());

    if (answers.length < questions.length) {
        ask(answers.length); // when array increases correlates to the next index of the questions array.
    } else {
        process.exit();
    }
});

// Handle process exit
process.on('exit', () => {
    const [name, activity, lang] = answers;
    console.log(`

    Thank you for your answers.

    Go ${activity} ${name} you can write ${lang} code later!!
    
    
    `)
});

// process.stdin.on('data', data => { // listens for data event -> typing something on keyboard
//     process.stdout.write(`\n\n ${data.toString().trim()}\n\n`);
//     process.exit();
// }); // Asynchronous, this process will keep running unless told otherwise. Will continue to listen for data until told to exit.