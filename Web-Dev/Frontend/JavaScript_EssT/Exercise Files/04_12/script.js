function doSomeMath() {
	var a = 5; // not accessbile once function is invoked.
	var b = 4;
	// var sum = a + b;
	//
	// return sum;

	// Closure:
	// This inisde function relies on variables that have been defined
	// in the outside function. Browser understand that these two are related,
	// so it keeps variables a & b "alive." that allows this function to work.
	function multiply() {
		var result = a*b;
		return result;
	}

	return multiply; // multiply holds the total function mutiply with all of
							     // its contents. It doesn't run the function.
}

var theResult = doSomeMath();

console.log("The result: ", theResult);
console.log("The result: ", theResult());

// ################ Second function using a closure ############################
function giveMeEms(pixels) {
	// Closure begins.
	var baseValue = 16;

	function doTheMath() {
		return pixels/baseValue;
	}

	return doTheMath;
	// Closure ends.
}

var smallSize = giveMeEms(12);
var mediumSize = giveMeEms(18);
var largeSize = giveMeEms(24);
var xlargeSize = giveMeEms(32);

console.log("Small size: ", smallSize());
console.log("Medium size: ", mediumSize());
console.log("Large size: ", largeSize());
console.log("Extra Large size: ", xlargeSize());





/**
	Closure.

	https://developer.mozilla.org/en/docs/Web/JavaScript/Closures

*/
