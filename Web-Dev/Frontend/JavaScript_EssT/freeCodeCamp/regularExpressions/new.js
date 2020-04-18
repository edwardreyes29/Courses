// Use lookaheads in the pwRegex to match passwords that are greater than 5 characters 
// long, do not begin with numbers, and have two consecutive digits.
let quit = "qu";
let noquit = "qt";
let quRegex= /q(?=u)/;
let qRegex = /q(?!u)/;
quit.match(quRegex); // Returns ["q"]
noquit.match(qRegex); // Returns ["q"]

let sampleWord = "astronaut";
let pwRegex = /^(?!\d)(?=[a-z]{3,})(?=\w*\d{2})/i; // Change this line
let result = pwRegex.test(sampleWord);

// Checks for Penguin or Pumpkin
let testStr = "Pumpkin";
let testRegex = /P(engu|umpk)in/;
testRegex.test(testStr);

// Hint 1

// Use a|b to check for either a or b.
// Hint 2

// Your regex should use mixed grouping like /P(engu|umpk)in/g.
// Hint 3

// Use .* to allow for middle names.
// Returns true
'let myString = "Eleanor Roosevelt";
let myRegex = /(Franklin|Eleanor).*Roosevelt/;
let result = myRegex.test(myString);'

// matches 10 10 10, 100 100 100, 42 42 42
let repeatNum = "42 42 42";
let reRegex = /^(\d+)(\s)\1\2\1$/; // Change this line
let result = reRegex.test(repeatNum);

freeCodeCamp.org

    /news
    /forum
    /learn

// Regular Expressions: Use Capture Groups to Search and Replace

// Searching is useful. However, you can make searching even more powerful when it also changes (or replaces) the text you match.

// You can search and replace text in a string using .replace() on a string. The inputs for .replace() is first the regex pattern 
// you want to search for. The second parameter is the string to replace the match or a function to do something.
let wrongText = "The sky is silver.";
let silverRegex = /silver/;
wrongText.replace(silverRegex, "blue");
// Returns "The sky is blue."

// You can also access capture groups in the replacement string with dollar signs ($).
"Code Camp".replace(/(\w+)\s(\w+)/, '$2 $1');
// Returns "Camp Code"


// Write a regex fixRegex using three capture groups that will search for each word in the string "one two three". 
// Then update the replaceText variable to replace "one two three" with the string "three two one" and assign the 
// result to the result variable. Make sure you are utilizing capture groups in the replacement string using the 
// dollar sign ($) syntax.

let str = "one two three";
let fixRegex = /(\w+)\s(\w+)\s(\w+)/; // Change this line
let replaceText = "$3 $2 $1"; // Change this line
let result = str.replace(fixRegex, replaceText);



// Write a regex and use the appropriate string methods to remove whitespace at the beginning and end of strings.

// Note: The String.prototype.trim() method would work here, but you'll need to complete this challenge using regular expressions.
let hello = "   Hello, World!  ";
let wsRegex = /^\s+|\s+$/g; // Change this line
let result = hello.replace(wsRegex, ""); // Change this line


