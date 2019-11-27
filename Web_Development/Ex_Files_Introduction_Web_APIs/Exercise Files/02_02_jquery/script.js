$.ajax ({
	url: 'https://hplussport.com/api/products',
	success: function(response) {
		console.log(response)
	}
})

// A method specifically for GET requests
$.get({
	url: 'https://hplussport.com/api/products',
	success: function(response) {
		console.log(response[0])
	}
})

