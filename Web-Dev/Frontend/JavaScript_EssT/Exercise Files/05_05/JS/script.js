/**
  <div class="cta">
    <a href="#">Book Now!</a>
  </div>
*/
const CTAELEMENT = document.querySelector(".cta a");
console.log(CTAELEMENT); // Returns <a href="#">Book Now!</a>

if (CTAELEMENT.hasAttribute("target")) {
  console.log(CTAELEMENT.getAttribute("target"));
} else {
    CTAELEMENT.setAttribute("target", "_blank"); // set attriubte with name and value of blank
}

console.log(CTAELEMENT.attributes); // returns attributes currently applied to this element
                                    // only attricute is the href, but after setting attr target
                                    // it now has two (href, target)
                                    
console.log(CTAELEMENT); // Returns <a href="#" target="_blank">Book Now!</a>
