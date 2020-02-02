// IV. Returning function & named function
function findBiggestFraction(a,b) {
    var result;
    a>b ? result = ["firstFraction", a] : result = ["secondFraction", b];
    return result
}

var firstFraction = 3/4;
var secondFraction = 5/7;

var fractionResults = findBiggestFraction(firstFraction,secondFraction);
console.log(fractionResults);


console.log("First fraction result: ", firstFraction);
console.log("Second fraction result: ", secondFraction);
console.log("Fraction " + fractionResults[0] + " with a value of " +
  fractionResults[1] + " the biggest!");
