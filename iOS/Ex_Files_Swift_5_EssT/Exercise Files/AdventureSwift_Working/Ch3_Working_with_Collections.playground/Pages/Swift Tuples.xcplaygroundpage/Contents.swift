/*:
 # Swift Tuples
 ---
 
 ## Topic Essential
 In Swift, tuples can take a group of values and store them as one compound value. Unlike arrays, tuples can store values of different types, so you can mix and match as much as you need.
 
 Tuples are great for returning values from functions, and storing temporary groups of values. However, as tempting as it may be to use tuples to create and store complex data structures, it’s still a better idea to use classes and structs for that, as we’ll see later on.
 
 ### Objectives
 + Create a simple tuple named **uppercutAttack** with initial values and no value names
 + Create another tuple named **planetSmashAttack** with initial values and value names
 + Create a final tuple named **shieldStompAttack** with no initial values and a type annotation
 + Explore what tuples have to offer
 
 [Previous Topic](@previous)                                                 [Next Topic](@next)

 */
// Simple tuple -> Store types in the order in which they appear
var uppercutAttack: (String, Int, Bool) = ("Uppercut Smash", 25, true)
uppercutAttack.0 // Name of attack
uppercutAttack.1 // Damage
uppercutAttack.2 // Rechargeable Property

// Unpack each tuple value into it's own name variable
var (attack, damage, rechagreable) = uppercutAttack
attack
damage
rechagreable

// Naming tuple values

// Either method allows you to get variables by name instead of by index or by manually unpacking the tuple
var shieldStomp: (name: String, damage: Int, rechargeable: Bool)
var planetSmash = (name: "Planet Smash", damage: 45, rechagreable: true)

shieldStomp.damage = 100
shieldStomp.rechargeable = true

// Naming values with type annotation

