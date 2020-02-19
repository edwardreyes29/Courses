
/**
  <div class="cta">
      <a href="#" class="hide">Book Now!</a>
      <section id="booking-alert" class="booking-info">
          <div class="centered">
              <h3 class="content-title">Sorry about that!</h3>
              <p class="teaser two-column">By some weird coincidence, all the rooms at Moonwalk Manor are booked out for the date you planned to take your trip. Unfortunately we are unable to provide you with sufficient lodging for your party at this time. Moonwalk Manor is very busy and your satisfaction is our top priority. When you take your first steps in the moon dust, your life will change. We are always at your service. Your satisfaction matters to us.</p>
          </div>
      </section><!-- .booking-info -->
  </div><!-- .cta -->
*/

const CTA = document.querySelector(".cta a");
const ALERT = document.querySelector("#booking-alert");

/*
  Make website resillient, meaning making page accesible
  when they don't have JS enabled.
*/

// If JS is enabled, then the book now is not hidden, but the alert is.
CTA.classList.remove("hide");
ALERT.classList.add("hide");

/*
  When an event like clock is fired,we can catch the event object as an
  attribute in the funciton that is trggered.
*/
function reveal(e) {
  // prevents the defulat behavior of the event object (clicked link)
  // This prevents the page from hopping back to the top, since the
  // the behavior of the a href is to go to a new link, but it goes back to
  // the currnt page.
  e.preventDefault();
  CTA.classList.toggle("hide");
  ALERT.classList.toggle("hide");


  console.log(e);
  console.log(CTA);
}

// Bind event to function.
CTA.onclick = reveal; /* By leaving out the parentheses, we ensure the function
                         when the script orignally loads. */
