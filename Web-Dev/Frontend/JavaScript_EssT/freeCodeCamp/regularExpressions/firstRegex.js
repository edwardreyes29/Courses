let myString = "Hello, World";
let myRegex = /Hello/;
let result = myRegex.test(myString);
console.log(result);

// match pets "dog", "cat", "bird", or "fish"
let petString = "James has a pet cat."
let petRegex = /dog|cat|bird|fish/;
result = petRegex.test(petString);
console.log(result);

// ignore case using i flag:
myString = "freeCODeCamp";
let fccRegex = /freeCodeCamp/i;
result = fccRegex.test(myString);
console.log(result);

// Find and Extract more than one match:

let twinkleStar = "Twinkle, twinkle, little star";
let starRegex = /twinkle/gi; // ignore case and find/extract pattern more than once
result = twinkleStar.match(starRegex);
console.log(result);

// Wildcard -> match strings "run", "sun", "fun", "pun", "nun", "bun"
let exampleStr = "Let's have fun wth regular expressions!";
let unRegex = /.un/; 
result = unRegex.test(exampleStr);
console.log(result);

// Character classes to match multiple possibilities:
let quoteSample = "Beware of bugs in the above code; I have only porved it correct, not tried it.";
let vowelRegex = /[aeiou]/gi;
result = quoteSample.match(vowelRegex);
console.log(result);

// use range to match letters:
quoteSample = "The quick brown fox jumps over the lazy dog.";
let alphabetRegex = /[a-z]/gi;
result = quoteSample.match(alphabetRegex);
console.log(result);