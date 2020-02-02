/*
  Anonymous functions
  var variable = function() {}
*/

var a = 5/7;
var b = 18/25;

var theBiggest = function(a,b) {
  var result;
  a>b ? result = ["a", a] : result = ["b", b];
  // console.log(result);
  return result;
}

var c = theBiggest(7/9,13/25); // Inside this variable thee is an anonymous functions
console.log(c);
