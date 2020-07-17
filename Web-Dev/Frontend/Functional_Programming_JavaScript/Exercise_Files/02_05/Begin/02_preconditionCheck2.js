// Learning Functional Programming with Javascript
// Chapter 02, Video 05, Exercise 02

function createSafeVersion(func) {
  return function(n, message) {
    if (n != null && typeof n === 'number') {
      if (message != null && typeof message === 'string') {
        return func(n, message)
      }
    }
  }
}

function printMessageNTimes(n, message) {
  for (var i = 0; i < n; i++) { console.log(message) }
}

function getNthLetter(n, string) {
  return string.charAt(n)
}

function getSubstringOfLength(n, string) {
  return string.substring(0, n)
}

var printMessageNTimesSafe = createSafeVersion(printMessageNTimes)
var getNthLetterSafe = createSafeVersion(getNthLetter)
var getSubstringOfLengthSafe = createSafeVersion(getSubstringOfLength)

// doIfSafe(4, "Banana", printMessageNTimes) // prints "Banana Banana Banana Banana"
// doIfSafe(2, "Javascript", getNthLetter) // 'v'
// doIfSafe(5, "Hello and welcome", getSubstringOfLength) // "Hello"
printMessageNTimesSafe(4, "Banana")
getNthLetterSafe(2, "JavaScript")
getSubstringOfLengthSafe(5, "Hello and welcome")

getNthLetterSafe("two", "JavaScript") // returns null