# Python - Async Comprehension

## Description
This project builds on asynchronous programming in Python by introducing asynchronous generators, async comprehensions, and running multiple coroutines in parallel to measure combined runtime.

In this project, we focus on:
- Writing asynchronous generators using `async def` combined with `yield`
- Using async comprehensions (`[x async for x in ...]`) to collect values from an async generator
- Running multiple coroutines in parallel with `asyncio.gather`
- Measuring the total runtime of parallel asynchronous executions
- Type-annotating asynchronous generators

The main goal of this project is to understand how asynchronous generators and comprehensions work, and how running coroutines concurrently affects total execution time compared to running them sequentially.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
   ```
2. Move into the project directory:
   ```
   cd holbertonschool-web_back_end/python_async_comprehension
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

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
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
| `0-async_generator.py` | Asynchronous generator that yields 10 random numbers, one per second |
| `1-async_comprehension.py` | Async comprehension that collects the 10 values from `async_generator` |
| `2-measure_runtime.py` | Runs `async_comprehension` four times in parallel with `asyncio.gather` and measures the total runtime |

## Notes
Running `async_comprehension` four times in parallel takes roughly 10 seconds in total, not 40. This is because `asyncio.gather` runs all four generators concurrently on the same event loop: while one coroutine is waiting (`await asyncio.sleep(1)`), the event loop switches to another coroutine and makes progress on it, instead of blocking. Since each generator's 10 iterations of 1-second waits overlap with the others, the total time stays close to the time of a single run (~10 seconds).

## Author
Rahaf Alabdalh
