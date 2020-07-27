'use strict';

// let clicks = {};

function updateClicks() { // updateClicks(menu)
  let clicks = {}; // can now be moved back to updateClicks() function
  // let button = menu.id; // id value of element clicked
  let button;
  // clicks[button] = clicks[button] + 1 || 1; // if key doesn't exist, set to one otherwise | create a key value pair
  
  /*
    The inner function has it's own scope and has access to variables in the parent function.
    Normally when a function is done executing, all of it's values are garbage collected by the parser.
    When since updateClicks() returns a reference to a function that has access to it's local variables, 
    when updateClicks() is returned, its references are not resolved but remain in memory, and the reference from
    those variables returned from the report function are called closure.
  */
  function reportClicks(menu) {
    button = menu.id; // id value of element clicked
    // const report = [button, clicks] // id, and the clicks variable
    clicks[button] = clicks[button] + 1 || 1; // if key doesn't exist, set to one otherwise | create a key value pair
    console.log(button, clicks); // ... will log both elements in array (ES6)
  }

  // reportClicks(); // updateClicks always calls this function
  return reportClicks;
}
/*
  since updateClicks() returns reportClicks, report variable stores a reference to the inner function
*/
const report = updateClicks(); 

const activities = {
  teamIn: ['basketball','hockey','volleyball'],
  teamOutWarm: ['softball/baseball','football/soccer','American football','rowing','tennis','volleyball','ultimate frisbee','rugby'],
  teamOutCold: ['hockey'],
  soloIn: ['rock climbing','swimming','ice skating'],
  soloOutWarm: ['rowing','running','hiking','cycling','rock climbing'],
  soloOutCold: ['snowshoeing','downhill skiing','cross-country skiing','ice skating']
};
let state = {};
let category = 'all';
let url = 'http://api.openweathermap.org/data/2.5/weather?q=';
let apiKey = "de36e36780976652d3e84a5502633fce"; // Replace "APIKEY" with your own API key; otherwise, your HTTP request will not work
function updateActivityList(event) {
  if (event !== undefined && event.target.classList.contains('selected')) {
    return true;
  } else if (event !== undefined && !event.target.classList.contains('selected')) {
    category = event.target.id;
    document.querySelectorAll('.options div').forEach(function(el) {
      el.classList.remove('selected');
    });
    event.target.classList.add('selected');
  } 

  state.activities = [];
  if (state.condition === "Rain") {
    updateState('In');
  } else if (state.condition === "Snow" || state.degFInt < 50) {
    updateState('OutCold');
  } else {
    updateState('OutWarm');
  }

  function updateState(type) {
    if (category === 'solo') {
      state.activities.push(...activities['solo' + type]);
    } else if (category === 'team') {
      state.activities.push(...activities['team' + type]);
    } else {
      state.activities.push(...activities['solo' + type]);
      state.activities.push(...activities['team' + type]);
    }
  }

  let activitiesContainer = `<ul>`;
  state.activities.forEach(function(activity,index) {
    activitiesContainer += `<li key="${index}">${activity}</li>`
  });
  activitiesContainer += `</ul>`;
  
  document.querySelector('.activities').innerHTML = activitiesContainer;
  document.querySelector('.results').classList.add('open');
}
function updateUISuccess(response) {
  const degC = response.main.temp - 273.15;
  const degF = degC * 1.8 + 32;
  state = {
    condition: response.weather[0].main,
    icon: 'https://openweathermap.org/img/w/' + response.weather[0].icon + '.png',
    degCInt: Math.floor(degC),
    degFInt: Math.floor(degF),
    city: response.name
  };

  document.querySelector('.conditions').innerHTML = `
    <p class="city">${state.city}</p>
    <p>${state.degCInt}\u00B0 C / ${state.degFInt}\u00B0 F
      <img src="${state.icon}" alt="${state.condition}">
    </p>
  `; 

  updateActivityList();
}
function updateUIFailure() {
  document.querySelector('.conditions').textContent = 'Weather information unavailable';
}

// get weather data when user clicks Forecast button, then add temp & conditions to view
document.querySelector('.forecast-button').addEventListener('click', function(e) {
  e.preventDefault();
  const location = document.querySelector('#location').value;
  document.querySelector('#location').value = '';
  fetch(url + location + '&appid=' + apiKey).then(function(response) {
    return(response.json());
  }).then(function(response) {
    updateUISuccess(response);
  }).catch(function() {
    updateUIFailure();
  });
}, false);

// update list of sports when user selects a different category (solo/team/all)
document.querySelectorAll('.options div').forEach(function(el) {
  el.addEventListener('click', function(event) {
    updateActivityList(event);
    // updateClicks(event.target);
    report(event.target);
  }, false);
});