# Bu bir deneme yorumudur
#!/usr/bin/env python3

import argparse
import sympy as sp
import logging


def integrate_expr(expr_str, var_str, lower=None, upper=None, add_constant=True):
    """
    Compute the integral of expr_str with respect to var_str.
    If lower and upper are provided, computes definite integral.
    Otherwise, computes indefinite integral and optionally adds constant C.
    """
    try:
        # Define the symbol
        var = sp.symbols(var_str)
        # Parse the expression
        expr = sp.sympify(expr_str)

        # Compute definite or indefinite integral
        if lower is not None and upper is not None:
            result = sp.integrate(expr, (var, lower, upper))
        else:
            result = sp.integrate(expr, var)
            if add_constant:
                C = sp.symbols('C')
                result += C
        return result
    except Exception as e:
        logging.error(f"Error integrating expression '{expr_str}': {e}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Compute definite or indefinite integrals using Sympy."
    )
    parser.add_argument(
        "--expr", "-e", required=True,
        help="The expression to integrate, e.g. 'sin(x)'"
    )
    parser.add_argument(
        "--var", "-v", default="x",
        help="Variable of integration (default: x)"
    )
    parser.add_argument(
        "--lower", "-l", type=float,
        help="Lower limit for definite integral"
    )
    parser.add_argument(
        "--upper", "-u", type=float,
        help="Upper limit for definite integral"
    )
    parser.add_argument(
        "--no-constant", dest="add_constant", action="store_false",
        help="Do not add integration constant C for indefinite integrals"
    )
    parser.add_argument(
        "--no-simplify", dest="simplify", action="store_false",
        help="Do not simplify the resulting expression"
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    try:
        result = integrate_expr(
            args.expr, args.var,
            lower=args.lower, upper=args.upper,
            add_constant=args.add_constant
        )
        if args.simplify:
            result = sp.simplify(result)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Failed to integrate expression: {e}")


if __name__ == "__main__":
    main()
