// Learning Functional Programming with Javascript
// Chapter 04, Video 02, Exercise 02

var x = 1

console.log("x is originally " + x)

setTimeout( function() {
    x = 99
    console.log("x has been changed, and is now " + x)
}, 3000)
// no guarantee what order either setTimeout functions will be executed in
setTimeout( function() {
    x = 100
    console.log("x has been changed, and is now " + x)
}, 3000)

// Nesting can have setTimeout functions execute in a particular order
setTimeout( function() {
    x = 100
    console.log("x has been changed, and is now " + x)
    setTimeout( function() {
        x = 200
        console.log("x has been changed, and is now " + x)
        setTimeout( function() {
            x = 300
            console.log("x has been changed, and is now " + x)
        }, 3000)
    }, 3000)
}, 5000)

console.log("x is " + x)