/*
  ES2015: let and const

  const:  Constant.
          Can't be changed once defined.

  let:    Block scope varaible.
          Smaller scope than var.
*/

// let
function logScope() {
  var localVar = 2;
  if (localVar) {
    // var localVar = "I'm different!"; // In this case, local var get reassigned.
    let localVar = "I'm different!"; // the scope is only within the conditional stmt.
    console.log("nested localVar", localVar);
  }

  console.log("logScope localVar: ", localVar);
}

logScope();

// Const
const MYCONSTANT = 5;
console.log(MYCONSTANT);
MYCONSTANT = 6; // Creates an ERROR.
