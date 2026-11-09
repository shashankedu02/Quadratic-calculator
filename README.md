# Quadratic Calculator (Python)

A small command-line tool for solving equations in the form:

```
ax² + bx + c = 0
```

It reports real or complex roots and rejects invalid equations where `a = 0`.

## Run

```bash
python quadratic_calculator.py
```

## Test

```bash
python -m unittest discover
```

## Example

For `x² - 5x + 6 = 0`, enter:

```
a = 1
b = -5
c = 6
```

The solutions are `x = 2` and `x = 3`.
