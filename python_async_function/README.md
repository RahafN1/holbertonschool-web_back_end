# Python - Async

## Description
This project introduces asynchronous programming in Python using the `asyncio` module. It covers writing and running coroutines, executing multiple coroutines concurrently, measuring runtime, and working with `asyncio` Tasks.

In this project, we focus on:
- Writing basic async coroutines with `async` / `await` syntax
- Running async programs with `asyncio.run()`
- Running concurrent coroutines with `asyncio.gather()`
- Measuring the total runtime of concurrent executions
- Creating and managing `asyncio.Task` objects
- Using the `random` module to introduce randomized delays

The main goal of this project is to understand how asynchronous execution works in Python, and how it differs from traditional synchronous, blocking code.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
   ```
2. Move into the project directory:
   ```
   cd holbertonschool-web_back_end/python_async_function
   ```
3. Make sure the files are executable:
   ```
   chmod +x *.py
   ```
4. Run any file directly, for example:
   ```
   ./0-main.py
   ```

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8
- `pycodestyle` (version 2.5.x)
- All files must start with `#!/usr/bin/env python3`
- All files must end with a new line
- All modules, functions, and coroutines must be documented with real sentences
- All functions and coroutines must be type-annotated

## Examples
```python
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

## Testing
Each task has a corresponding `N-main.py` test file used to validate functionality. To test:
```
./N-main.py
```
Do not include additional test files in the final repository unless required.

## Files
| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | Basic async coroutine with a random delay |
| `1-concurrent_coroutines.py` | Executes multiple coroutines concurrently |
| `2-measure_runtime.py` | Measures the total runtime of concurrent coroutines |
| `3-tasks.py` | Creates an `asyncio.Task` from a coroutine |
| `4-tasks.py` | Executes multiple tasks concurrently |

## Author
Rahaf Alabdalh
