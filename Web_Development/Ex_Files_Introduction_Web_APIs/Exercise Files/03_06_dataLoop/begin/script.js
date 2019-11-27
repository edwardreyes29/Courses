var request = new XMLHttpRequest();

request.open('GET', 'https://hplussport.com/api/products?order=name');

request.onload = function() {
	var response = request.response;
	var parsedData = JSON.parse(response);
	console.log(parsedData);
	

	// Display name of all products & image
	// Create a loop
	for(item in parsedData) {
		var name = parsedData[item].name;
		var products = document.createElement('li');
		products.innerHTML = name;
		document.body.appendChild(products);

		// Show price
		var price = parsedData[item].price;
		var prices = document.createElement('li');
		prices.innerHTML = '$' + price;
		document.body.appendChild(prices);

		var imageURL = parsedData[item].image;
		var images = document.createElement('img');
		images.setAttribute('src', imageURL);
		document.body.appendChild(images);

		// Add description
		var description = parsedData[item].description;
		var descriptions = document.createElement('p');
		descriptions.innerHTML = description + '\n';
		document.body.appendChild(descriptions);

		
	}

};

request.send();