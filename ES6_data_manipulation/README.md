      # ES6 Data Manipulation

## Description
This project covers data manipulation in modern JavaScript (ES6). It focuses on working with arrays and the newer built-in data structures that ES6 introduced, such as typed arrays, `Set`, `Map`, and `WeakMap`.

In this project, we focus on:

- Using `map`, `filter`, and `reduce` on arrays
- Creating and using typed arrays (`Int8Array`, `ArrayBuffer`, `DataView`)
- Working with the `Set` data structure
- Working with the `Map` data structure
- Understanding the `WeakMap` (weak link) data structure

The main goal of this project is to be able to explain and use these tools to store, transform, and query data efficiently, without relying on external help.

## Learning Objectives
At the end of this project, you should be able to explain:

- How to use `map`, `filter`, and `reduce` on arrays
- What typed arrays are and how to use them
- How the `Set`, `Map`, and `WeakMap` data structures work

## Requirements
- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files must end with a new line
- All files use the `.js` extension
- Code is tested with **Jest** and linted with **ESLint** (Airbnb base config)
- All functions must be exported

## Installation
Clone the repository:

```bash
git clone https://github.com/RahafN1/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end/ES6_data_manipulation
```

Install the dependencies:

```bash
npm install
```

## Usage
Create a main file (for example `0-main.js`) and run it with Babel:

```bash
npm run dev 0-main.js
```

### Example

```javascript
import getListStudents from './0-get_list_students.js';

console.log(getListStudents());
```

Output:

```
[
  { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
  { id: 2, firstName: 'James', location: 'Columbia' },
  { id: 5, firstName: 'Serena', location: 'San Francisco' }
]
```

## Testing
Run the tests:

```bash
npm run test
```

Run the linter and the tests together:

```bash
npm run full-test
```

## Files

| File | Description |
|------|-------------|
| `0-get_list_students.js` | Returns a list of student objects (`id`, `firstName`, `location`) |
| `1-get_ids.js` | Returns an array of student ids using `map` |
| `2-get_students_by_loc.js` | Returns students from a given city using `filter` |
| `3-get_ids_sum.js` | Returns the sum of all student ids using `reduce` |
| `4-update_grade_by_city.js` | Updates the grades of students in a city by combining `filter` and `map` |
| `5-typed_arrays.js` | Creates an `Int8Array` in an `ArrayBuffer` and sets a value at a given position |
| `6-set.js` | Creates a `Set` from an array |
| `7-has_array_values.js` | Checks whether a `Set` contains all values of an array |
| `8-clean_set.js` | Returns a string of `Set` values that start with a given prefix |
| `9-groceries_list.js` | Returns a `Map` of groceries and their quantities |
| `10-update_uniform_items.js` | Updates the quantity of items in a `Map` |
| `100-weak.js` | Uses a `WeakMap` to track and limit the number of API calls per endpoint |

## Project Structure

```
ES6_data_manipulation/
├── README.md
├── package.json
├── babel.config.js
├── .eslintrc.js
├── 0-get_list_students.js
├── 1-get_ids.js
├── 2-get_students_by_loc.js
├── 3-get_ids_sum.js
├── 4-update_grade_by_city.js
├── 5-typed_arrays.js
├── 6-set.js
├── 7-has_array_values.js
├── 8-clean_set.js
├── 9-groceries_list.js
├── 10-update_uniform_items.js
└── 100-weak.js
```

## Resources
- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
- [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)

## Author
Rahaf Alabdalh