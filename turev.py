import sympy as sp


def differentiate_expr(expr_str, var_str):
    """
    Compute the derivative of expr_str with respect to var_str.
    """
    try:
        # Parse the expression
        expr = sp.sympify(expr_str)

        # Determine differentiation variable
        var = sp.symbols(var_str)

        # Compute the derivative
        derivative = sp.diff(expr, var)
        return derivative
    except Exception as e:
        raise ValueError(f"Error differentiating expression '{expr_str}': {e}")


def differentiate_second_expr(expr_str, var_str):
    """
    Compute the second derivative of expr_str with respect to var_str.
    """
    try:
        # Parse the expression
        expr = sp.sympify(expr_str)

        # Determine differentiation variable
        var = sp.symbols(var_str)

        # Compute the second derivative
        second_derivative = sp.diff(expr, var, 2)
        return second_derivative
    except Exception as e:
        raise ValueError(f"Error differentiating expression '{expr_str}': {e}")


def main():
    expr = input("Enter the expression to differentiate: ")
    var = input("Enter the variable of differentiation: ")
    
    # First derivative
    first_result = differentiate_expr(expr, var)
    print(f"The first derivative of {expr} with respect to {var} is: {first_result}")

    # Second derivative
    second_result = differentiate_second_expr(expr, var)
    print(f"The second derivative of {expr} with respect to {var} is: {second_result}")


if __name__ == '__main__':
    main()