/*:
 # Core Set Methods
 ---
 
 ## Topic Essentials
 Because sets only store unique values, there are a number of useful operations you can perform on them without having to reinvent the sorting/filtering wheel. These include the `intersection` and difference of set values, as well as `union` and `subtraction`. 
 
 ### Objectives
 + Copy and paste the **allQuests** set from the previous page
 + Create a new set called **completedQuests** and assign it a subset of quests from **allQuests**
 + Try out the different operations the `Set` class can perform
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Test variables
var activeQuest: Set = ["Fetch Gemstones", "Big Boss" , "The Undertaker", "Granny Needs Firewood"]
var completedQuests: Set = ["Big Boss", "All-4-One", "The Hereafter"]

// Set operations

// Return common values b/w both sets [Intersection] (A ^ B)
var commonQuests = activeQuest.intersection(completedQuests)

// Return quests not in both (A (+) B)
var differentQuests = activeQuest.symmetricDifference(completedQuests)

// Union set, all values from both sets
var allQuests = activeQuest.union(completedQuests)

