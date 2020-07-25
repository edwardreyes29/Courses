// Learning Functional Programming with Javascript
// Chapter 03, Video 06, Exercise 01
var _ = require("lodash")

var employees = [
  { name: "John",   salary: 60000,  age: 27, gender: 'M' },
  { name: "Mary",   salary: 110000, age: 50, gender: 'F' },
  { name: "Susan",  salary: 50000,  age: 21, gender: 'F' },
  { name: "Greg",   salary: 100000, age: 45, gender: 'M' },
  { name: "Jerry",  salary: 90000,  age: 39, gender: 'M' },
  { name: "Barb",   salary: 95000,  age: 36, gender: 'F' }
]

// filter array for male employees
var males = _.filter(employees, function(employee) {
  return employee.gender === 'M'
}) // returns array of males

// Convert male array to ages of all male employees
var maleAges = _.map(males, function(male) {
  return male.age
})

// Find total age
var maleAgeTotal = _.reduce(maleAges, function(acc, age) {
  return acc + age
})

// Get average age for males
var maleAgeAverage = maleAgeTotal / males.length

console.log(maleAgeAverage)

// Filter array for female employees
var females = _.filter(employees, function(employee) {
  return employee.gender === 'F'
})

// Convert female array to ages of all male employees
var femaleAges = _.map(females, function(female) {
  return female.age
})

// find total age for females
var femaleAgeTotal = _.reduce(femaleAges, function(acc, age) {
  return acc + age
})

// get average age for females
var femaleAgeAverage = femaleAgeTotal / females.length

console.log(femaleAgeAverage)

/*

  Notes:
  - many transformations, common practice for functional programming.
  - Original data has not been mutated, maintained integrity of original data

*/
