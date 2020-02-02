function findBiggestFraction() {
  a>b ? console.log("a: ", a) : console.log("b: ", b);
}

// Works while these variables are declare before calling function.
// However, this is considered bad practice
var a = 3/4;
var b = 5/7;

findBiggestFraction();
