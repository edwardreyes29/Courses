/*
  Immediately invoked functional expressions
    var variable = (function(params...) {
      ...
    }(args...))

  In anonymous functions, variables contain the function & can be seen in console.
  The browser runs the function once it encounters it.

  Why use it?
    It runs immeeiately where it is located in the code
    Great for quickly populating an argument
*/

var firstFraction = 7/9;
var secondFraction = 13/25;

var theBiggest = (function(a,b) {
  var result;
  a>b ? result = ["a", a] : result = ["b", b];
  return result;
})(firstFraction, secondFraction);

console.log(theBiggest)
