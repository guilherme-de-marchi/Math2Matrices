# Math2Matrices

## Getting started

### How to use

Download this repositore, put the archive ```math2matrices.py``` in your project and import it. 
```python
from math2matrices import Matrix
```

How create a matrix object:
```python
Matrix([
  [1, 2, 3], # Each list is a line
  [3, 2, 1], # And each item inside the list is a column
  [2, 1, 3],
])

# If you want to make a list integrally of a value...
Matrix(2, (3, 3)) # The tuple(x, y) represents the size of your matrix
# Returns -> Matrix object
# [[2, 2, 2],
#  [2, 2, 2],
#  [2, 2, 2]]
```

Doing calculations:
```python
A = Matrix(2, (3, 3))
B = Matrix(1, (3, 3))

A + B
# Or Matrix.add(A, B)
# [[3, 3, 3],
#  [3, 3, 3],
#  [3, 3, 3]]
```
