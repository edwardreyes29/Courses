const CTA = document.querySelector(".cta a");
const ALERT = document.querySelector("#booking-alert");

CTA.classList.remove("hide");
ALERT.classList.add("hide");

function reveal(e) {
    e.preventDefault();
    CTA.classList.toggle("hide");
    ALERT.classList.toggle("hide");
}

// CTA.onclick = reveal;

//  monitor click event, bind it t reveal function, and define how to define event.
// last parameter is only relevant when you're piling on events.Use false unless
// your using really advanced JavaScript.
// This allows us to stack multiple functions to the same interaction.
CTA.addEventListener("click", reveal, false)
CTA.addEventListener("click", function() { console.log("The button was clicked!");}, false);







// Create a second event to see what happens
/* The second event is taking precedence over the first one.
  So entire script is broken. */
// CTA.onclick = console.log("The button was clicked!");

// Can't add more events, but another way to add events to functions is to
// use EventListeners.
