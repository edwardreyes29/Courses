/*:
 # Core Array Methods
 ---
 
 ## Topic Essentials
 Now that we know how to create and access arrays, we need to learn how to dynamically modify them. Like `Strings`, `Arrays` come with several handy methods built right in for just that purpose.
 
 ### Objectives
 + Create an array called **characterClasses** and assign it initial values
 + Use `append` and += operator to add items
 + Use the `insert` and `remove` methods to change the array further
 + Explore the `reverse`, `contains`, and`sort` methods
 + Create a jagged array called **skillTree** that stores arrays as its values
 + Use chained **subscript syntax** to access a value in **skillTree**
 
  [Previous Topic](@previous)                                                 [Next Topic](@next)
 
 */
// Changing & appending items
var characterClasses = ["Solo", "Netrunner", "Engineer"]
characterClasses.append("Rockerboys")
characterClasses += ["Techie" , "Nomads"]


//Inserting and removing items , Dynamic modifications
characterClasses.insert("Journalist", at: 2) // doesn't replace, adds journalist, shifts elements after to the right

characterClasses.remove(at: 3) // removes 'Engineer'


// Ordering and querying values
characterClasses.reverse() // doesn't change original array

var reversedClasses = characterClasses.reversed() // Good practice to keep original data

characterClasses.sort()
var sortedClasses = characterClasses.sorted()

characterClasses.contains("Nomads")

print(characterClasses)

// 2D arrays and subscripts -> Jagged arrays: arrays that store arrays as their values
// As long as arrays store the same type, compiler is happy
var skillTree: [[String]] = [
    ["Attack+", "Barrage", "Heavy Hitter"],
    ["Guard+", "Evasion", "Run"]
]

var attackTreeSkill = skillTree[0][2] // Get third item

