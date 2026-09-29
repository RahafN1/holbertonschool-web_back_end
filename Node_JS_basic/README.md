# Node JS Basics

## Description
This project introduces the basics of Node.js. It covers running JavaScript with Node, using built-in modules, reading files (synchronously and asynchronously), accessing command line arguments and the environment through `process`, and building HTTP servers with both the Node `http` module and Express.

In this project, we focus on:

- Running JavaScript using Node.js
- Using Node.js modules
- Reading files with the `fs` module
- Using `process` to access command line arguments and the environment
- Creating a small HTTP server using Node.js
- Creating a small HTTP server and advanced routes using Express
- Using ES6 with Babel-node
- Using Nodemon to develop faster

## Installation
1. Clone the repository:
   `git clone https://github.com/RahafN1/holbertonschool-web_back_end.git`
2. Move into the project directory:
   `cd holbertonschool-web_back_end/Node_JS_basic`
3. Install the dependencies:
   `npm install`
4. Run a file:
   `node 0-main.js`

## Requirements
- Ubuntu 20.04 LTS
- Node.js 20.x.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All files end with a new line
- Code uses the `.js` extension
- Code is verified with ESLint
- All functions/classes are exported using `module.exports = myFunction;`

## Examples
```javascript
const displayMessage = require('./0-console');

displayMessage('Hello NodeJS!');
```

Output:
```
Hello NodeJS!
```

## Testing
Run the tests and the linter with:
```bash
npm run test
npm run full-test
```

## Files
| File | Description |
|------|-------------|
| `0-console.js` | Prints a string to STDOUT |
| `1-stdin.js` | Reads user input using `process.stdin` |
| `2-read_file.js` | Reads a file synchronously and counts students |
| `3-read_file_async.js` | Reads a file asynchronously and counts students |
| `4-http.js` | Small HTTP server using Node's `http` module |
| `5-http.js` | More complex HTTP server using Node's `http` module |
| `6-http_express.js` | Small HTTP server using Express |
| `7-http_express.js` | More complex HTTP server using Express |
| `full_server/` | Organized Express server (controllers, routes, utils) |
| `database.csv` | Students data used by the project |
| `package.json` | Project dependencies and scripts |
| `babel.config.js` | Babel configuration |
| `.eslintrc.js` | ESLint configuration |

## Author
Rahaf Alabdalh