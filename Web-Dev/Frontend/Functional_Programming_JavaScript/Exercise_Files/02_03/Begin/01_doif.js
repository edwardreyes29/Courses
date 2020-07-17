// Learning Functional Programming with Javascript
// Chapter 02, Video 03, Exercise 01


function doIf(condition, func) {
  if (condition) {
    func()
  }
}

const x = 1

// if (x === 1) {
//   sayXis1()
// }

// doIf(x === 1, sayXis1)

doIf(x === 1, function() { // Anonymous function, function without a name
  console.log("x is equal to 1")
})

// if (x === "Bananas") {
//   sayXisBananas()
// }

// doIf(x === "Bananas", sayXisBananas) 

doIf(x === "Bananas", function() {
  console.log("x is equal to 'Bananas'")
})

// if (x < 10 && x > 0) {
//   sayXisBetween0And10()
// }

doIf(x < 10 && x > 0, sayXisBetween0And10)

// function sayXis1() { console.log("x is equal to 1") }

// function sayXisBananas() { console.log("x is equal to 'Bananas'") }

function sayXisBetween0And10() { console.log("x is between 0 and 10") }
