var request = new XMLHttpRequest();

request.open('GET', 'https://hplussport.com/api/products?qty=2&order=name');

request.onload = function() {
	var response = request.response;
	var parsedData = JSON.parse(response);
	console.log(parsedData);
	// Cam access keys and properties using dot notation
	// Response comes in as an array. Access product at index 0
	var description = parsedData[0].description;
	console.log(description);
	
	var id = parsedData[1].id;
	console.log(id);

	var price = parsedData[1].price;
	console.log(price);

	var image_title = parsedData[0].image_title;
	console.log(image_title);
};

request.send();