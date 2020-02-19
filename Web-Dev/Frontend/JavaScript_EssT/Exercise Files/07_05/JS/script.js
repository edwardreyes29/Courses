const CTA = document.querySelector(".cta a");
const ALERT = document.querySelector("#booking-alert");

CTA.classList.remove("hide");
ALERT.classList.add("hide");

function reveal(e,current) {
    e.preventDefault();
    // CTA.classList.toggle("hide");
    current.innerHTML == "Book Now!" ? CTA.innerHTML = "Oooops!" : CTA.innerHTML = "Book Now!";
    ALERT.classList.toggle("hide");

    //  cannot turn off default behavior.
}

// reveal function, add ability to add arguments.
// But if parentheses is added, function will run when called.
// You could add an anonymous funciton within the reveal function and pass
// arguments there.
// (!) this -> referes object that was just clicked
// pass e (the event object) from the anonymous function
CTA.addEventListener('click', function(e){ reveal(e, this); }, false);
CTA.addEventListener('click', function(){
  console.log("The button was clicked!")}, false);
