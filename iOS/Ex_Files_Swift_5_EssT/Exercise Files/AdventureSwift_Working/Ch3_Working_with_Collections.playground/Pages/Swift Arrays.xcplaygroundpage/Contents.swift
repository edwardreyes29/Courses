/*:
 # Swift Arrays
 ---
 
 ## Topic Essentials
 Swift arrays are **ordered lists**, meaning that the position of each element is determined by the order it was added. Arrays work off of indexes, which can be used to access and modify the values of individual items.
 
 ### Objectives
 + Create arrays with different syntax
 + Add initial values
 + Use the `count` and `isEmpty` methods
 + Access and update array values using subscripts
 
 [Next Topic](@next)
 
 */
// Creating arrays
var levelDifficulty: [String] = ["Easy", "Moderate", "Veteran", "Nightmare"]
var extraSyntax1: Array<String> = Array<String>() // Both are treated the same by compiler

// Count and isEmpty
levelDifficulty.count
levelDifficulty.isEmpty

// Accessing array values
var mostDifficult = levelDifficulty[3]
levelDifficulty[3] = "Utter Ridiculousness"
print(mostDifficult)
print(levelDifficulty[3])

// Review
var monthlyIncome: [Double] = [949.47, 234.32, 426.64, 433.43, 353.57]
print(monthlyIncome[1])

var dogNames: [String]
dogNames = ["Scooby-doo", "Snoopy", "Balto"]
print(dogNames[dogNames.count - 1])
