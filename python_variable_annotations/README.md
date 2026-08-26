# Python - Variable Annotations

## Description
This project is an implementation of **type-annotated Python functions and variables**, using Python 3's typing system. Type annotations allow developers to specify the expected types of function arguments, return values, and variables, making code more readable, self-documenting, and easier to validate with static type checkers like `mypy`.

In this project, we focus on:
- Adding type annotations to function signatures
- Annotating variables with their expected types
- Using complex types (`List`, `Tuple`, `Union`, `Sequence`, `Callable`, etc.) from the `typing` module
- Understanding duck typing in Python
- Validating annotated code using `mypy`

The main goal of this project is to understand how type annotations work in Python 3 and how they help write safer, more maintainable code.

## Installation
Clone the repository:
```bash
git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
```

Move into the project directory:
```bash
cd holbertonschool-web_back_end/python_variable_annotations
```

Make the files executable:
```bash
chmod +x *.py
```

Run any file directly:
```bash
./0-add.py
```

## Requirements
- Ubuntu 20.04 LTS
- Python 3.9
- pycodestyle (version 2.5)
- mypy (for type checking, task 12)

### General
- All files are interpreted using `python3` (version 3.9)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style guide
- All files are executable
- All modules, classes, and functions are documented with real, descriptive docstrings
- All functions and coroutines are type-annotated

## Files

| File | Description |
| --- | --- |
| `0-add.py` | Type-annotated function that adds two floats |
| `1-concat.py` | Type-annotated function that concatenates two strings |
| `2-floor.py` | Type-annotated function that returns the floor of a float |
| `3-to_str.py` | Type-annotated function that converts a float to a string |
| `4-define_variables.py` | Defines and annotates variables with their respective types |
| `5-sum_list.py` | Type-annotated function that sums a list of floats |
| `6-sum_mixed_list.py` | Type-annotated function that sums a mixed list of ints and floats |
| `7-to_kv.py` | Type-annotated function that returns a tuple from a string and int/float |
| `8-make_multiplier.py` | Type-annotated function that returns a function multiplying a float |
| `9-element_length.py` | Type-annotated function using duck typing on an iterable object |
| `100-safe_first_element.py` | Duck-typed function returning the first element of a sequence |
| `101-safely_get_value.py` | Function with more involved/advanced type annotations |
| `102-type_checking.py` | Corrected code validated using `mypy` type checking |

## Examples

```python
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)
```

Output:
```
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

## Testing
You can test each function by creating a `X-main.py` file and running it directly:
```bash
./0-main.py
```

You can validate type annotations using `mypy`:
```bash
mypy 102-type_checking.py
```

## Learning Objectives
By the end of this project, you should be able to explain, without the help of Google:
- Type annotations in Python 3
- How to use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Author
- **Rahaf Alabdalh**