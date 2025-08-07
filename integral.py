# Bu bir deneme yorumudur
#!/usr/bin/env python3

"""
A command-line tool to compute definite or indefinite integrals using Sympy.
Features:
 - Accepts numeric or symbolic integration limits
 - Auto-detects integration variable if not provided
 - Optional integration constant for indefinite integrals
 - Simplification of results (configurable)
 - Output in plain text or LaTeX format
 - Logging of process and timing
"""
import argparse
import sympy as sp
import logging
import time
import sys


def integrate_expr(expr_str, var_str=None, lower=None, upper=None, add_constant=True):
    """
    Compute the integral of expr_str with respect to var_str.
    If lower and upper are provided, computes definite integral.
    Otherwise, computes indefinite integral and optionally adds constant C.
    Limits (lower/upper) and var_str can be symbolic strings.
    """
    try:
        # Parse the expression
        expr = sp.sympify(expr_str)

        # Determine integration variable
        if var_str:
            var = sp.symbols(var_str)
        else:
            symbols = list(expr.free_symbols)
            if len(symbols) == 1:
                var = symbols[0]
                logging.info(f"Auto-detected integration variable: {var}")
            else:
                raise ValueError("Could not auto-detect variable. Please specify --var.")

        # Parse limits if provided
        if lower is not None and upper is not None:
            lower_lim = sp.sympify(lower)
            upper_lim = sp.sympify(upper)
            result = sp.integrate(expr, (var, lower_lim, upper_lim))
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
        "--var", "-v", 
        help="Variable of integration (default: auto-detect)"
    )
    parser.add_argument(
        "--lower", "-l",
        help="Lower limit for definite integral (numeric or symbolic)"
    )
    parser.add_argument(
        "--upper", "-u",
        help="Upper limit for definite integral (numeric or symbolic)"
    )
    parser.add_argument(
        "--no-constant", dest="add_constant", action="store_false",
        help="Do not add integration constant C for indefinite integrals"
    )
    parser.add_argument(
        "--no-simplify", dest="simplify", action="store_false",
        help="Do not simplify the resulting expression"
    )
    parser.add_argument(
        "--format", "-f", choices=["str", "latex"], default="str",
        help="Output format: plain string or LaTeX"
    )
    parser.add_argument(
        "--log-level", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level"
    )
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="[%(levelname)s] %(message)s"
    )

    # Validate limits: require both or none
    if (args.lower is None) ^ (args.upper is None):
        logging.error("Both --lower and --upper must be provided for a definite integral.")
        sys.exit(1)

    # Compute integration
    try:
        start_time = time.time()
        result = integrate_expr(
            args.expr, args.var,
            lower=args.lower, upper=args.upper,
            add_constant=args.add_constant
        )
        elapsed = time.time() - start_time
        logging.info(f"Integration completed in {elapsed:.4f} seconds.")

        # Simplify if desired
        if args.simplify:
            result = sp.simplify(result)

        # Format output
        if args.format == "latex":
            output = sp.latex(result)
        else:
            output = str(result)

        print(f"Result: {output}")
    except Exception as e:
        print(f"Failed to integrate expression: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
