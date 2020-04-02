let myString = "Hello, World";
let myRegex = /Hello/;

// console.log(myRegex.test(myString));

let petString = "James has a pet cat.";
let petRegex = /dog|cat|bird|fish/i;

// console.log(petRegex.test(petString));

let quoteSample = "Beware of bugs in the above code; I have only proved it correct";
let vowelRegex = /[aeiou]/gi;

// console.log(quoteSample.match(vowelRegex));

quoteSample = "The quick brown fox jumps over the lazy dog.";
let alphabetRegex = /[a-z]/gi;

// console.log(quoteSample.match(alphabetRegex));

