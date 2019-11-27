// Fetch is built upon JavaScript promises
// fetch resources asynchronously across the network using url
fetch('https://hplussport.com/api/products')
.then( // does something with repsonse, can change multipel mehtods
	function(response) {
		return response.json(); // .json() to get json data
	}
)
.then(
	function(respData) {
		console.log(respData); // then get data to print
	}
)