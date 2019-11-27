/*:
 # Unwrapping Optionals
 ---
 
 ## Topic Essentials
 Optional unwrapping uses a variation of the if statement to safely check for nil values without crashing the code. If a value exists it will be stored in a local variable that's only accessible within the body of the if statement.

 
 ### Objectives
 + Use optional binding to unwrap a single optional
 + Unwrap multiple optionals in a single line of code for more compact structure
 + Unwrap nested optional values
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Test variables
var itemGathered: String? = "Diamond Longsword" // Optional value
var isShopOpen: Bool? = true

// Dictionary
var blacksmithShop: [String: Int] = ["Bottle": 10, "Shield": 15, "Ocarina": 100]
// Nested Dictionary
var questDirectory = [
    "Fetch Gemstones": [
        "Objective": "Retrieve 5 gemstones",
        "Secret": "Complete in under 5 minutes"
    ],
    "Defeat Big Boss": [
        "Objective": "Beat the ultimate boss",
        "Secret": "Win with 50% health left"
    ]
]

// Optional binding
// "If itemGathered is not nil, unwrap value and assign it to nil
if let item =  itemGathered {
    // item is now an unwrapped value
    print("You found a \(item)") // item is only accesible in this if statement
} else { // Handle nil value
    print("Sorry, no item found")
}

// Unwrap multiple optionals at the same time, use a shorthand syntax
// They both need to be non-nil
if let shopOpen = isShopOpen, let searchedItem = blacksmithShop["Shield"] {
    print("We're open \(shopOpen) and we have a \(searchedItem) in stock!")
} else {
    print("Sorry, either we're not open or don't have your item...")
}

// Look up "Fetched Gemstones" dictionary and add ? to denote it as an optional, it might not exist
// if it does, query the "Objective"
if let fetchedGems = questDirectory["Fetched Gemstones"]?["Objective"] {
    // If found
    print("Active quest: \(fetchedGems)")
} else {
    print("That quest is no longer available")
}



// [notes]
// Optional -> type that represents iether a wrapped value or a nil, the absence of a value
// Optional type: Wrapped type Int? == Optional<Int>
// Enumerations of two cases. Optional.non is nil, Optional.some(Wrapped) stroes some wrapped value
// Uses: Getting a dictionary's value using a key returns an optional value.
// e.g.  imagePath["star"] has type Optional<String> or String?
