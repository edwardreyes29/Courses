const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

module.exports = (mathQuestions, evaluate) => {
    const variables = [];
    const [firstVariable] = mathQuestions; // get first variables

    const variableEntered = vars => {
        variables.push(vars);

        if (variables.length < mathQuestions.length) {
            rl.question(mathQuestions[variables.length], variableEntered);
        } else {
            evaluate(variables);
        }
    };

    rl.question(firstVariable, variableEntered);
};