// Learning Functional Programming with Javascript
// Chapter 02, Video 04, Exercise 01

/*
  Currently no private variables in JavaScript
  Use closure to implement private variables
*/

// JavaScript object
// const myCounter = {
//   count: 0,
//   increment: function() {
//     this.count += 1
//   },
//   currentValue: function() {
//     return this.count
//   }
// }

function createCounter() {
  var count = 0
  return { // This is what myCounter really is, and it does not have property count
    increment: function() {
      count += 1  // Count is captured in the two functions here
    },
    currentValue: function() {
      return count
    }
  }
}

var myCounter = createCounter()

console.log(myCounter.currentValue())

myCounter.increment()
myCounter.increment()

console.log(myCounter.currentValue())

myCounter.count = 999 // uh oh!
// myCounter.count can no longer be referenced
// myCounter does not currently have a property called count

console.log(myCounter.currentValue())
