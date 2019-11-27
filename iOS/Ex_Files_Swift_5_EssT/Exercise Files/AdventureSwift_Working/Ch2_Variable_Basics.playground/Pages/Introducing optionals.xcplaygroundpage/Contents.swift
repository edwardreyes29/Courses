/*:
 # Introducing Optionals
 ---
 
 ## Topic Essentials
 Optional variables tell the compiler that the variable is either storing a value or storing nothing, which is really useful when you need placeholders for potentially unknown values.
 
 ### Objectives
 + Create two optional variables of different types
 + Use force unwrapping and understand the dangers of using it
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

*/
// Creating optionals
var itemGathered: String? = "Pickaxe" // mark as optional with question mark
var isExchangeable: Bool? // both stored as nil


// Forced unwrapping
print(itemGathered) // Need to unwrap, item gathered has not been unwrapped
print(itemGathered!) // Forced unwrapping, assumes you know the optional variable is not nil -> don't form a habit for force unwrapping
//print(isExchangeable!)
