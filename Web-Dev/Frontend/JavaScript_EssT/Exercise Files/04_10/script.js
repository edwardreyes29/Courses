// capital for creating an object.
function Course(title,instructor,level,published,views) {
  this.title = title; // similar to Java.
  this.instructor = instructor;
  this.level = level;
  this.published = published;
  this.views = views;
  this.updateViews = function() {
    return ++this.views;
  }
}

// Create an array that holds all the courses.
var courses = [
  new Course("JS ESST Training", "Morten Rand-Hendriksen", 1, true, 0),
  new Course("Up and Running with ECMAScript 6", "Eve Porcello", 1, true, 123456)
]

console.log(courses);
console.log(courses[1].instructor); // Retrieve name of instructor from second course.
console.log(courses[0].updateViews()); // Update view of first course.

// // Create a new instance of the Course object.
// var course01 = new Course("JS ESST Training", "Morten Rand-Hendriksen", 1, true, 0);
// console.log(course01);
// // Create a second instance of the Course object.
// var course02 = new Course("Up and Running with ECMAScript 6", "Eve Porcello", 1, true, 123456);
// console.log(course02);

/**
  Object constructors.
*/
