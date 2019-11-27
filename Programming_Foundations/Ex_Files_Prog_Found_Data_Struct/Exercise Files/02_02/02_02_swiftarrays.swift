 // import Foundation
var perStudentPetCount = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

var numOfStudents = perStudentPetCount.count

// sumOfItems / numOfStudents

print(perStudentPetCount[3])
// print(perStudentPetCount[100])
print(numOfStudents)

var sum = 0

// Just like in python, individualPetCount receives each element in array
// for x in seq:
// 		sum += x
for individualPetCount in perStudentPetCount {
	sum = sum + individualPetCount
}

print(sum)

var average = sum / numOfStudents

print(average)