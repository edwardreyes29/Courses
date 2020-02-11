
/*
<figure class="story-wrapper">
    <img src="images/testimonials/bluepebble.jpg" alt="">
    <figcaption class="story">
        <h3 class="story-header">Earth Rise</h3>
        <div class="author">Bob MacEnzie</div>
        <p>You've heard stories about the first astronauts visiting the moon and looking back at the earth rising on the horizon. Then you see it for yourself and realize just how small and vulnerable we all are.</p>
        <a href="#" class="content-button">Get the whole story</a>
    </figcaption>
</figure>
*/

const FEATURED = document.querySelector(".story-wrapper"); /* one constant for
figure*/
console.log(FEATURED);
const THEIMAGE = FEATURED.querySelector("img"); /* one constant for image inside
figure*/
THEIMAGE.alt = "Earthrise: photo of the earth from the moon";

// Get image alt attr
var altText = THEIMAGE.getAttribute("alt");
console.log(altText);

// Create figcaption elements
var captionElement = document.createElement("figcaption");
console.log(captionElement); /* Creates a figcaption documnet that is not placed
anywhere in the document */

// // Create Text Node to hold Alt text and place into new variable
// var captionText = document.createTextNode(altText);
//
// // Open caption Text Node inside the caption element.
// captionElement.appendChild(captionText); // only accpets type node (Text Node)
// console.log(captionElement);
//
//
// // Then appendChild to .storywrapper
// FEATURED.appendChild(captionElement);

/* Use new append method to replace two previous code (may be supported by all
browsers) */
captionElement.append(altText); /* automatically places altText within
figcpation as a Text Node */
FEATURED.append(captionElement);

/*
<figure class="story-wrapper">
    <img src="images/testimonials/bluepebble.jpg" alt="">
    <figcaption class="story">
        <h3 class="story-header">Earth Rise</h3>
        <div class="author">Bob MacEnzie</div>
        <p>You've heard stories about the first astronauts visiting the moon and looking back at the earth rising on the horizon. Then you see it for yourself and realize just how small and vulnerable we all are.</p>
        <a href="#" class="content-button">Get the whole story</a>
    </figcaption>
    <figcaption>Earthrise: photo of the earth from the moon</figcaption>
</figure>
*/


// Finally, grab the image, set attribute Alt to nothing.
THEIMAGE.setAttribute("alt", "");


// New method appendChild
// Rerence: https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/append
