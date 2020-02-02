/*
  Variable Scope

  Two types:
    1. Global
      - Can access anywhere in the JavaScript.
      - Is saved for as long as the script runs
        e.g. firstFractoin & secondFraction are global variables.
    2. Local
      - Only available within a block of code  like in a function.
      e.g. result is a local variable, and only accessible within the
           findBiggestFraction function.

    (!) Don't make all variables global.
    Local variables only exists for as long as the function runs and then
    the browser discards them Immediately. They can be used over and over again.
*/

function findBiggestFraction(a,b) {
    console.log("Fraction a: ", firstFraction);
    console.log("Fraction b: ", secondFraction);

    var result;

	a>b ? result = ["a",a] : result = ["b",b];
    return result;
}

var firstFraction = 7/16;
var secondFraction = 13/25;

var fractionResult = findBiggestFraction(firstFraction,secondFraction);
console.log("Fraction " + fractionResult[0] + " with a value of " + fractionResult[1] + " is the biggest.");
console.log(result); // produces and error because it is outside of it's scope
