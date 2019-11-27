// Create XMLHttpRequest object
var request = new XMLHttpRequest(); 

// open connection to make request
// 1st param: type of request, 2nd param: url making request to
request.open('GET', 'https://hplussport.com/api/products') 

// write function to do something with data
// onload event will run a functions once request has completed
request.onload = function() {
   // Get response, which is data from API
   var response = request.response
   // Parse data from string to object
   var parsedData = JSON.parse(response);	
   console.log(parsedData);
}

request.send(); 