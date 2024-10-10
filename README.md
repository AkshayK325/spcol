# spcol (B-spline collocation matrix) for B-Spline Basis and Derivative Computation 

## Overview

This Python script provides a set of functions to compute B-spline basis functions, their derivatives, and construct a collocation matrix for a set of input points. The script can be used for applications involving B-splines, such as numerical methods, interpolation, or computer-aided design (CAD). 

## Features
- **B-spline basis function computation**: The `N` function computes the B-spline basis functions using Cox-de Boor recursion formula.
- **First derivative of the B-spline basis functions**: The `dN` function computes the first derivative of the B-spline basis functions.
- **Higher-order derivatives**: The `ddN` function computes higher-order derivatives of the B-spline basis functions.
- **Knot span locator**: The `findspan` function finds the knot span for a given value of the parameter.
- **Collocation matrix construction**: The `spcol` function constructs a collocation matrix for a set of input values (`u`) based on the B-spline basis functions and their derivatives.

## Functions

### `N(x, d, i, t)`
Calculates the B-spline basis function `N_i^d(x)` recursively:
- `x`: The input parameter.
- `d`: Degree of the B-spline.
- `i`: Index of the basis function.
- `t`: Knot vector.

### `dN(x, d, i, t)`
Computes the first derivative of the B-spline basis function `N_i^d(x)`:
- Same parameters as `N(x, d, i, t)`.

### `ddN(x, d, i, t, k)`
Calculates the `k`th derivative of the B-spline basis function `N_i^d(x)`:
- `x`: The input parameter.
- `d`: Degree of the B-spline.
- `i`: Index of the basis function.
- `t`: Knot vector.
- `k`: Order of the derivative.

### `findspan(t, x)`
Finds the knot span for a given input `x` in the knot vector `t`:
- `t`: Knot vector.
- `x`: The input parameter.

### `spcol(U, d, u)`
Constructs the collocation matrix for a given set of input parameters `u`:
- `U`: Knot vector.
- `d`: Degree of the B-spline.
- `u`: Array of input points.

## Example Usage

Below is a simple example of how to use the script:

```python
iimport numpy as np
import matplotlib.pyplot as plt

# Assuming the spcol function is imported from your file
from spcol import spcol

# Knot vector
U = np.array([0, 0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1, 1])
# Degree of the B-spline
p = 3
# Input points where we want to evaluate the B-spline curve
u = np.linspace(0,1,100)

# Control points for the B-spline in 2D (x, y)
XY = np.array([[0.0, 0.0],   # Control point 1 (x1, y1)
               [1.0, 1.0],   # Control point 2 (x2, y2)
               [2.0, 1.0],   # Control point 3 (x3, y3)
               [3.0, 2.0],   # Control point 4 (x4, y4)
               [4.0, 1.0],   # Control point 5 (x5, y5)
               [5.0, 0.0],   # Control point 6 (x6, y6)
               [1.0, 0.0]])  # Control point 7 (x7, y7)

# Generate the collocation matrix M
M = spcol(U, p, u)

# Calculate the xy coordinates of the B-spline at points u
xy = M @ XY  # Matrix multiplication (M * control points)

# Extract the x and y values
x_vals = xy[:, 0]
y_vals = xy[:, 1]


# Generate the collocation matrix M
M = spcol(U, p, np.unique(U))

# Calculate the xy coordinates of the B-spline at points u
xy = M @ XY  # Matrix multiplication (M * control points)

# Extract the x and y values
x_valsKnots = xy[:, 0]
y_valsKnots = xy[:, 1]

# Plotting
plt.figure()
# Plot the control polygon (control points)
plt.plot(XY[:, 0], XY[:, 1], 'o--', label='Control Polygon', color='grey')
# Plot the B-spline curve (evaluated points)
plt.plot(x_vals, y_vals, 'r-', label='B-spline Curve')
plt.scatter(x_valsKnots, y_valsKnots,c='b',marker="s", label='Knots')
plt.title("B-spline Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
```

## Requirements

- Python 3.x
- NumPy

You can install the required dependencies via pip:

```bash
pip install numpy
```

## License
This script is provided "as is" without any warranty. Feel free to modify and use it for educational or research purposes.

## Author

- **akshaykumar@wisc.edu**  
  Created on: October 20, 2021
  
Feel free to reach out for any questions or clarifications!
