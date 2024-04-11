
# Pascal's Triangle

## Description
This Python function `pascal_triangle(n)` generates Pascal's triangle up to the specified number of rows `n`. Pascal's triangle is a triangular array of binomial coefficients, where each number is the sum of the two directly above it in the previous row.

## Installation
This function does not require any installation. Simply copy the function definition into your Python project

## Usage
To use the `pascal_triangle(n)` function, follow these steps:

1. Import the function into your Python script or interactive session.
   ```python
   from pascal_triangle import pascal_triangle
   ```

2. Call the function with the desired number of rows (`n`) as an argument.
   ```python
   triangle = pascal_triangle(5)
   ```

3. Use the returned list of lists to access Pascal's triangle.
   ```python
   print(triangle)
   ```

   Output:
   ```
   [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
   ```

## Examples
```python
from pascal_triangle import pascal_triangle

# Example 1: Generating Pascal's triangle with 5 rows
triangle_5 = pascal_triangle(5)
print(triangle_5)
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Example 2: Generating Pascal's triangle with 0 rows (returns an empty list)
triangle_0 = pascal_triangle(0)
print(triangle_0)
# Output: []
```

## Contact
For questions or inquiries, please contact Nonkuu at nonku.yandah@gmail.com
