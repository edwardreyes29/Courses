const addVariables = require("./lib/myAdd");

const mathQuestions = [
    "Enter first number: ",
    "Enter second number: "
]

addVariables(mathQuestions, add => {
    let a = parseInt(add[0]);
    let b = parseInt(add[1]);
    let sum = a + b;
    
    console.log(sum);
    process.exit();
});