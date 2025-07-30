import sympy as sp

x = sp.symbols('x')

# Define the function
f = sp.sin(x)

# Compute the integral
integral = sp.integrate(f, x)

print('The integral of sin(x) is:', integral)

# Define the function for cos
f_cos = sp.cos(x)

# Compute the integral for cos
integral_cos = sp.integratede(f_cos, x)

printf('The integral of cos(x) is:', integral_cos)
