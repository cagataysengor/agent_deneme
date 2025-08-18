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


def main():
    expr = input("Enter the expression to differentiate: ")
    var = input("Enter the variable of differentiation: ")
    result = differentiate_expr(expr, var)
    print(f"The derivative of {expr} with respect to {var} is: {result}")


if __name__ == '__main__':
    main()