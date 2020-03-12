// tabbed panels

// declare globals to hold all the links and all the panel elements
var tabLinks; // will hold tab elements
var tabPanels; // will hold tab panel elements

// When window loads, start this function
window.onload = function() {
  // set initial panel state
  // listen for clicks on tabs

  // get all list items within element with id tabs
  tabLinks = document.getElementById("tabs").getElementsByTagName("li");

  // console.log(tabLinks);

  // get all div elements withing container.
  tabPanels = document.getElementById("containers").getElementsByTagName("div");

  // console.log(tabPanels);

  // activate the _first_ one
  // set initial display of the active tab
  displayPanel(tabLinks[0]);

  // Attach event listener to links using onclick and onfocus,
  // fire the displayPanel function, return false to disable the link
  for (var i = 0; i < tabLinks.length; i++) {
    tabLinks[i].onclick = function() {
      // create an onclick and assign a function, when click run a function
      // console.log(this); // <li id="tab1..3"
      displayPanel(this); // this reference object that called function
      return false; // disable link that clicked
      /*
        For non javaScript users, clicking a tab returns a link that
        shifts the page to a particular section. Returning false disables
        that. Not sure why yet.

        https://stackoverflow.com/questions/8941626/onclick-function-is-not-blocking-the-href-value-of-anchor-tag-on-returning-true

        "even handler needs to return false to preven normal link action"
      */
    };

    /*
      onfocus event occurs when an element gets focus.active
      used with <inpu> <select> and <a>

      for keyboard or assistive technology.
    */
    tabLinks[i].onfocus = function() {
      displayPanel(this);
      return false;
    };
  }
};

function displayPanel(tabToActivate) {
  // respond to tab clicks
  // change panel display and activate tabs

  // go through all the <li> elements
  for (var i = 0; i < tabLinks.length; i++) {
    if (tabLinks[i] == tabToActivate) {
      // if it's the one to activate, change its class
      tabLinks[i].classList.add("active"); // no use yet...
      // and display the corresponding panel;
      tabPanels[i].style.display = "block";

      console.log(tabLinks[i]);
    } else {
      // remove the active class on the link
      tabPanels[i].classList.remove("active");
      // hide the panel
      tabPanels[i].style.display = "none";
    }
  }
}
