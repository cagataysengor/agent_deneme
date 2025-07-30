import sympy as sp

x = sp.symbols('x')

# Define the function
f = sp.sin(x)

# Compute the integral
integral = sp.integrate(f, x)

print('The integral of sin(x) is:', integral)