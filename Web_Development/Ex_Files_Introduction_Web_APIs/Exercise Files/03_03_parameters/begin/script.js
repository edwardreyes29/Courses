var request = new XMLHttpRequest();

// request.open('GET', 'https://hplussport.com/api/products?qty=2&order=name');

// request.onload = function() {
// 	var response = request.response;
// 	var parsedData = JSON.parse(response);
// 	console.log(parsedData);
// };

// request.send();

// request.open('GET', 'https://hplussport.com/api/products?id=526');

// request.onload = function() {
// 	var response = request.response;
// 	var parsedData = JSON.parse(response);
// 	console.log(parsedData);
// }

// request.send();

// request.open('GET', 'https://hplussport.com/api/products?order=price&sort=asc&qty=5');

// request.onload = function() {
// 	var response = request.response;
// 	var parsedData = JSON.parse(response);
// 	console.log(parsedData);
// }

// request.send();

request.open('GET', 'https://hplussport.com/api/products?page=3&qty=4');

request.onload = function() {
	var response = request.response;
	var parsedData = JSON.parse(response);
	console.log(parsedData);
}

request.send();

