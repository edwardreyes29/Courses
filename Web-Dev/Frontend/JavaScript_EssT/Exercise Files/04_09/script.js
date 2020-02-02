/*
  Make sense of objects.

  Array is an object.

  Objects are used to create cluster of related data and perform some
  actions or operations on that data.

  "Objects are data models that allow us to combine properties and methods
  for a specific data set in a structured way."

*/

var course =  new Object();

course.title = "JavaScript Essential Training";
course.instructor = "Morten Rand-Hendriksen";
course.level = 1;
course.published = true;
course.views = 0;

var myself = new Object();
myself.name = "Edward Reyes";
myself.major = "Computer Science";
myself.age = 28;

// Shorthand
var car = {
  brand: "Toyota",
  model: "Corolla",
  year: "2013",
  color: "blue",
  mileage: 0,
  updateMileage: function() {
    return ++car.mileage;
  }
}
console.log(car);
console.log(car.brand);
console.log(car.model);
console.log(car.year);
console.log(car.updateMileage());
