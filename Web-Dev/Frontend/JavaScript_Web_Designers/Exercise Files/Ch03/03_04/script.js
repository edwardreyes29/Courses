/*
    Listen to the submit event
*/
(function() {
"use strict";

    document.getElementById("cart-hplus").addEventListener('submit', estimateTotal); // get form id, add event listener for submit

    // Create function estimateTotal
    function estimateTotal(event) {
        // Stop page from reloading
        event.preventDefault(); // prevents any default action that would happen. In the case of submit, it prevents the page from reloading

        console.log('You submitted the form');
    }

})();

