# ES6 Classes

## Description
This project covers how classes work in ES6 (ECMAScript 2015). Before ES6, JavaScript relied on prototypes and constructor functions to simulate object-oriented patterns. ES6 introduced the `class` syntax, giving a cleaner and more familiar way to create objects, add methods, use inheritance, and work with getters/setters and static methods.

In this project, we focus on:

- Defining a class
- Adding instance methods to a class
- Adding static methods to a class
- Using getters and setters
- Extending a class from another (inheritance)
- Metaprogramming and symbols

The main goal of this project is to understand how the `class` syntax works under the hood, and how it compares to ES5 prototype-based patterns.

## Installation
Clone the repository:
```
git clone https://github.com/RahafN1/holbertonschool-web_back_end.git
```

Move into the project directory:
```
cd holbertonschool-web_back_end/ES6_classes
```

Install dependencies:
```
npm install
```

## Requirements
- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x
- Code is tested with the Jest Testing Framework
- Code is analyzed with ESLint (airbnb-base config)
- All files end with a new line
- All files use the `.js` extension

## Usage
Run a file with Babel node:
```
npm run dev <filename>.js
```

Run the linter:
```
npm run lint
```

Run the tests:
```
npm test
```

Run lint + tests together:
```
npm run full-test
```

## Files

| File | Description |
| --- | --- |
| `0-classroom.js` | Defines a `ClassRoom` class with a `maxStudentsSize` attribute |
| `1-make_classrooms.js` | Creates an array of multiple `ClassRoom` instances |
| `2-hbtn_course.js` | A `HolbertonCourse` class with getters and setters |
| `3-currency.js` | A `Currency` class with methods and computed method names |
| `4-pricing.js` | A `Pricing` class using `Currency` |
| `5-building.js` | A `Building` class with an abstract-like method |
| `6-sky_high.js` | A `SkyHighBuilding` class extending `Building` (inheritance) |
| `7-airport.js` | An `Airport` class using `Symbol.toStringTag` |
| `8-primitive_geometry.js` | A `HolbertonClass` using `Symbol.toPrimitive` |
| `9-hoisting.js` | Fixing hoisting issues in class-related code |
| `10-vault.js` | A `Vault` class using a private/closure-based field |
| `100-evcar.js` | An `EVCar` class extending `Car` (advanced inheritance) |

## Author
Rahaf Alabdalh