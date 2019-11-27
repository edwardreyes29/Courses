var dinnerChoices = [["Salad", "Soup", "Cheese Plate"], ["Chicken", "Salmon", "Lasagna"]]

let appIndex = 0        // Represents Appetizers
let mainDishIndex = 1   // Represents Main Dishes

let firstApp = dinnerChoices[appIndex][0] // First appetizer
let secondApp = dinnerChoices[appIndex][1] // Second appetizer
let thirdMainDish = dinnerChoices[appIndex][2] // Third appetizer

console.log(firstApp)
console.log(secondApp)
console.log(thirdMainDish)

dinnerChoices[mainDishIndex][0] = "Steak"
console.log(dinnerChoices[mainDishIndex][0])
console.log(dinnerChoices)