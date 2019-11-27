/*:
 # Working with Sets
 ---
 
 ## Topic Essentials
 Sets are a great tool you need to store unique, unorderd values in a collection, as opposed to arrays and dictionaries which can hold duplicates with no issue.
 
 ### Objectives
 + Create a set named **activeQuests** and understand the syntax
 + `insert` and `remove` elements from **activeQuests**
 + Sort **activeQuests** and check if it `contains` a certain value
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Type inference different with other types seen. Compiler can correclty infer from initial values that we want a set of Strings <String>
// We always need the 'Set' type to tell compiler that this is not an array

// Creating sets -> Also use brackets
// elements are present only once, (unique values), doesn't care about order
var activeQuests: Set<String> = ["Fetch Gemstones", "Big Boss", "The Undertaker", "Granny Needs Firewood"] // Want a set of strings; same syntax as arrays

var activeQuests2: Set = ["Fetch Gemstones", "Big Boss", "The Undertaker", "Granny Needs Firewood"]

// Removing items is efficient, no need to worry about indexes or referencing key value pairs
// Inserting and removing elements
activeQuests.insert("Only the Strong")
activeQuests.remove("The Undertaker")

print(activeQuests)

// More common methods
activeQuests.contains("All-4-One")

// Can sort set
activeQuests.sorted()

// Sets can only store values that are hashable -> They are able to provide a hash value themselves










// Review

// <Array>
var days: [String] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

// <Dictionary>
var seasons: [Int: String] = [1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"]
print(seasons[1])

// <Sets>
var elements: Set<String> = ["a", "b", "c"]
