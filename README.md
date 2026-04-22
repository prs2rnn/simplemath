# SimpleMath

A lightweight Python package with basic mathematical functions.

## Features

* Factorial calculation (iterative and recursive)
* Fibonacci calculation (sequence and generator)
*

## Installation

```shell
pip install git+https://github.com/prs2rnn/simplemath.git
```

## Usage

```python
from simplemath.fibonacci import FibonacciCalculator

# Fibonacci generator
fib_gen = FibonacciCalculator.generator()
first_10 = [next(fib_gen) for _ in range(10)]
```
