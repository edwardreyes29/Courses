// Regular function, called explicitly by name:
function multiply() {
    var result = 3 * 4;
    console.log("3 multiplied by 4 is ", result);
}
multiply();

// Anonymous function stored in variable.
// Invoked by calling the variable as a function:
var divided = function() {
    var result = 3 / 4;
    console.log("3 divided by 4 is ", result);
}
divided();

// Immediately Invoked Function Expression.
// Runs as soon as the browser finds it:
(function() {
    var result = 12 / 0.75;
    console.log("12 divided by 0.75 is ", result);
}())


// Named Function
function divide(a, b) {
  var result = a / b;
  console.log("[E.R] " + a + " divided by " + b + " is " + result);
}

divide(3, 4);

// Anonymous Functions
var multiply = function(a, b) {
  var result = a * b;
  console.log("[E.R] " + a + " multiplied by " + b + " is " + result);
}

multiply(3, 4);

// Immediatley invoked function expressions
(function() {
  var a = 3;
  var result = a * a;
  console.log("[E.R] " + a + " squared is " + result);
}())
