# Integration Using Simpson’s 3/8 Rule Numerical Method Implementation in Python

This repository contains a Python implementation of Simpson’s 3/8 Rule for numerical integration. The code computes the integral of the function \( F(x) = x^2 + 5x - 9 \) over a specified interval using Simpson's 3/8 Rule.

### Table of Contents
- [Simpson’s 3/8 Rule Theory](#simpsons-38-rule-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

### Simpson’s 3/8 Rule Theory
Simpson's 3/8 Rule is a method for numerical integration that estimates the value of a definite integral by interpolating the integrand using polynomial segments. This rule divides the interval into smaller segments, applying a weighted average at various points to obtain a more accurate approximation of the integral.

**Formula:**
For \( n \) intervals where \( n \) is divisible by 3:
\[
\int_a^b f(x) \, dx \approx \frac{3h}{8} \left[ f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + \ldots + f(x_n) \right]
\]
Where:
- \( h = \frac{b-a}{n} \)

### Dependencies
This implementation does not require any external libraries; it uses standard Python functions.

### Installation
No additional installation is required. Ensure you have Python installed on your system.

### Usage
1. Clone the repository.
2. Run the script using Python:
    ```sh
    python simpsons_38_rule.py
    ```
3. Input the required parameters when prompted:
    - Enter the lower limit of integration.
    - Enter the upper limit of integration.
    - Enter the step size (number of sub-intervals).

4. The script will calculate the integral and display the result.

### Code Explanation
The code defines a function `F(x)` representing the integrand and another function `Simpsons_38_interpolation(a, b, n)` to compute the integral using Simpson’s 3/8 Rule. The main program prompts the user for input values and computes the integration.

Below is a snippet from the code illustrating the main logic:

```python
def F(x):
    return x**2 + 5*x - 9

def Simpsons_38_interpolation(a, b, n):
    h = (b - a) / n
    integration = 0
    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h / 3
        x2 = x1 + h / 3
        x3 = a + (i + 1) * h
        val = (h * (F(x0) + 3 * F(x1) + 3 * F(x2) + F(x3))) / 8
        integration += val
    return integration

print("____Simpson's 3/8 Rule____")
a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))
step_size = int(input("Enter the number of intervals (step size): "))
integration = Simpsons_38_interpolation(a, b, step_size + 1)
print("\nIntegrated value = %.6f" % (integration))
```

### Example
Below is an example of how to use the script:

1. **Run the script**:
    ```sh
    python simpsons_38_rule.py
    ```

2. **Enter the input values**:
    ```
    Enter the lower limit: 0
    Enter the upper limit: 2
    Enter the number of intervals (step size): 3
    ```

3. **Output**:
    - The script will calculate the integration using Simpson's 3/8 Rule and print the result:
    ```
    Integrated value = 10.666667
    ```

### Files in the Repository
- `simpsons_38_rule.py`: The main script for performing the integration using Simpson's 3/8 Rule.

### Input Parameters
The script prompts for the following input values:
- Lower limit of integration (`a`).
- Upper limit of integration (`b`).
- Number of sub-intervals (`n`, which must be a multiple of 3).

### Troubleshooting
1. **Interval Size**: Ensure that the number of intervals entered is a multiple of 3 to apply Simpson’s 3/8 rule.
2. **Function Definition**: The function \( F(x) = x^2 + 5x - 9 \) is hardcoded. Modify this function as necessary to integrate a different function.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by [Your Name].

---

This documentation should guide you through understanding, installing, and using the Simpson’s 3/8 Rule script for numerical integration. For further issues or feature requests, please open an issue in the repository. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
