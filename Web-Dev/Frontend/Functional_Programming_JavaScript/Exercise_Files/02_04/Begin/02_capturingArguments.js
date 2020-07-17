// Learning Functional Programming with Javascript
// Chapter 02, Video 04, Exercise 02

// More Object-Oriented
function createCounter(count) {
  // var count = startAt

  return {
    increment: function() {
      count = count + 1
    },

    currentValue: function() {
      return count
    }
  }
}

/*
  If the outer function has arguments, the inner function has access to them as well
*/

var counterStartingAt5 = createCounter(5)

var counterStartingAtMinus2 = createCounter(-2)