var request = new XMLHttpRequest();

request.open('GET', 'https://hplussport.com/api/products?qty=2&order=name');

request.onload = function() {
	var response = request.response;
	var parsedData = JSON.parse(response);
	console.log(parsedData);
	var name = parsedData[0].name;

	// Create and element in html
	var products = document.createElement('li');
	products.innerHTML = name;
	document.body.appendChild(products);

	// Add description and price
	// var descript = parsedData[0].description;
	// var textnode = document.createTextNode(descript);
	// document.body.appendChild(textnode);	
	// var price = parsedData[0].price;
	// textnode = document.createTextNode(price);
	// document.body.appendChild(textnode);

};

request.send();