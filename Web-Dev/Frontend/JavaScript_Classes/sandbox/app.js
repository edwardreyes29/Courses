/* Causes an error, since classes are not hoisted on the top at compile time*/
// const cx5 = new Car(4, 'V6', 'red');
// console.log(cx5);
// console.log(cx5.carStats());
let mixin = {
    madeIn() {
        console.log('This car was made in year 2019!')
    }
}

let carMixin = {
    __proto__: mixin,

    madeIn() {
        super.madeIn();
    }
}

sayHi();

class Car { // not hoisted to the top
    constructor(doors, engine, color) {
        this.doors = doors;
        this.engine = engine;
        this.color = color;
    }

    carStats() {
        return `This car has ${this.doors} doors, a ${this.engine} engine and a beautiful ${this.color} color!`;
    }

    static totalDoors(car1, car2) {
        return car1.doors + car2.doors;
    }
}

const cx5 = new Car(4, 'V6', 'red');
const civic = new Car(2, '4C', 'silver');

console.log(cx5);
// console.log(cx5.carStats());
// console.log(civic);
// console.log(civic.carStats());
// console.log(Car.totalDoors(cx5, civic))

function sayHi() { // will be hoisted to the top 
    return console.log('Hello this function an be called anywhere');
}

class SUV extends Car {
    constructor(doors, engine, color, brand, carStats) {
        super(doors, engine, color, carStats);
        this.brand = brand;
        this.wheels = 4; // created when object is created.
        this.ac = true;

        // Not inheritance, but composition
        // assign mixin
        Object.assign(this, carMixin);
    }

    myBrand() {
        return console.log(`This SUV is a ${this.brand}`);
    }

    
}

const cx7 = new SUV(4, 'V6', 'grey', 'mazda');
console.log(cx7);
cx7.myBrand();
cx7.madeIn();