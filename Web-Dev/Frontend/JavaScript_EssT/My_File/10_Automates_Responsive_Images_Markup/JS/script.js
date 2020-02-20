/**
  Use loops to solve problem to manage responsive images markup wihout
  writing huge amounts of HTML.

  Courses: Responsive images.

  Use JS to inject responsive images code into HTML on the fly.

  1. Make changes to html to ensure images are not downloaced unless JS
     is not enabled.
  2. Find images in the page, loop through all of them, and retrieve Original
     image reference, generate repsonisve markup, and inject back into the page.
*/

/**
  images are all set to 800 by default, just incase JS is not enabled.
*/

// Create an array that contains all the images on the page.
const IMAGES = document.querySelectorAll("img");

// sizes attr: allows us to tell browser how wide images in comparision to viewport.
const SIZES = {
  showcase: "100vw",
  reason: "(max-width: 799px) 100vw, 372px",
  feature: "(max-width: 799px) 100vw, 558px",
  story: "(max-width: 799px) 100vw, 670px",
};

// using the srcset
function makeSrcset(imgSrc) {
    let markup = [];
    let width = 400; // smallest size

    for (let i = 0; i<5; i++) {
      markup[i] = imgSrc + "-" + width +".jpg " + width + "w";
      width+=400;
    }

    return markup.join(); // use join to return a comma separated list!
}

for (let i = 0; i < IMAGES.length; i++) {
  let imgSrc = IMAGES[i].getAttribute("src");
  // Strip the last few characters (-800.jpg) by using slice method
  imgSrc = imgSrc.slice(0, -8); // Go to end of array and strip out last 8 characters.
  let srcset = makeSrcset(imgSrc);
  // console.log(srcset);
  IMAGES[i].setAttribute("srcset", srcset);


  // call datatype getAttribute
  let type = IMAGES[i].getAttribute("data-type");
  // console.log(type);
  let sizes = SIZES[type];
  // console.log(sizes);
  IMAGES[i].setAttribute("sizes", sizes);


  // reference: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img

  /**
    Result:
    <img src="images/mainpromo/welcome02-800.jpg" alt="" data-type="reason"
    srcset="images/mainpromo/welcome02-400.jpg 400w,
    images/mainpromo/welcome02-800.jpg 800w,
    images/mainpromo/welcome02-1200.jpg 1200w,
    images/mainpromo/welcome02-1600.jpg 1600w,
    images/mainpromo/welcome02-2000.jpg 2000w"
    sizes="(max-width: 799px) 100vw,372px">
  */

}
