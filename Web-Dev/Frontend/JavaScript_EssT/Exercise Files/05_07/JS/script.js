// document.querySelector(".cta a").style.color = "green";
//
// // in CSS, use camelcase for certain CSS properties.
// document.querySelector(".cta a").style.backgroundColor = "blue";
//
//
// // To add multi-style properties, group in single string using CSS text property.
// document.querySelector(".cta a").style.cssText = "padding: 1em; color: white; background-color: red;"

// use attribute methods for a particular element.
document.querySelector(".cta a").setAttribute("style","padding: 2em");

// Add long string of differenct CSS properties.
document.querySelector(".cta a").setAttribute("style",
"padding: 2em; color: purple; background-color: gold;"); // no camel case in CSS style text
