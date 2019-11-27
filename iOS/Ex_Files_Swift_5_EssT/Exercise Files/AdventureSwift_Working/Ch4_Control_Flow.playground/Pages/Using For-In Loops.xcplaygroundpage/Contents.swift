/*:
 # Using FOR-IN Loops
 ---
 
 ## Topic Essentials
 For-in loops are used primarily to iterate, or loop through, sequences. Sequences can be array items, dictionary key-value pairs, ranges, and even characters in a string.
 
 ### Objectives
 + Use a for-in loop to iterate over a string, array, dictionary, and index ranges
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Test variables
let playerGreeting = "Hello fellow Hunter!"
let armorTypes = ["Heavy Plate", "Hunters Gear", "Mage Robes"]
let weapons = ["Longsword": 150, "Dagger": 25, "Mace": 75]

// Strings and arrays

// "Loop thorugh each value in playerGreeting string, store value in stringCharacter each time, and print
for stringCharacter in playerGreeting { // Swift will infer correct type
    print(stringCharacter)
}

for armor in armorTypes {
    print(armor)
}

// Dictionary key-value pairs
for weaponKey in weapons.keys { // use .keys to get keys
    print(weaponKey)
}

for weaponValues in weapons.values { // use .keys to get keys
    print(weaponValues)
}

// Display both
for (weapon, damage) in weapons { // decomoposing each key-value pari into elements of a tuple
    print("\(weapon): \(damage)")
}

// Using ranges
// Three types: 1. closed 2. half-open 3. one-sided

 // 1. closed range -> includes first number & last number and prints everything else inbetween
for indexNumber in 1...10 {
    // for every number in 1 through 10, print -> actually prints 1, 2,..., 10
    // in python, range(1,10) prints 1, 2,..., 9
    print(indexNumber)
}

// 3. One-sided ranges.
for armor in armorTypes[0...] { // for every armor in armorTypes, starting at first item [0], print
    print(armor)
}

// (!) Can cause infinite loops if sequence doesn't have set number of items
// Ex. This will go one forever
//for indexNumber in 1... {
//    print(indexNumber)
//}

// Half open range, last value is left out bascially
for indexNumber in 1..<10 { // two .. instead of three i closed-range and one-sided range ...
    print(indexNumber) // prints out 1, 2,..., 9
}

for armors in armorTypes[..<armorTypes.count] { // could give number that index exceed the number of items in collection
    print(armors)
}

