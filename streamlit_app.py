import streamlit as st
import sympy as sp
import logging

# Configure logging
type_map = {True: "on", False: "off"}
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def compute_integral(expr_str, var_str, lower, upper, definite, add_constant, simplify_res):
    """
    Compute definite or indefinite integral of an expression.
    """
    try:
        var = sp.symbols(var_str)
        expr = sp.sympify(expr_str)

        if definite:
            a = float(lower)
            b = float(upper)
            result = sp.integrate(expr, (var, a, b))
        else:
            result = sp.integrate(expr, var)
            if add_constant:
                C = sp.Symbol('C')
                result = result + C

        if simplify_res:
            result = sp.simplify(result)

        return result

    except Exception as e:
        logging.error(f"Error computing integral: {e}", exc_info=True)
        st.error(f"Error: {e}")
        return None


def main():
    st.title("Integral Calculator")
    st.write("Compute definite and indefinite integrals using Sympy and Streamlit.")

    # User inputs
    expr_str = st.text_input("Function expression (in terms of x):", "sin(x)")
    var_str = st.text_input("Variable of integration:", "x")
    definite = st.checkbox("Definite Integral", value=False)

    lower = upper = None
    if definite:
        col1, col2 = st.columns(2)
        lower = col1.text_input("Lower limit:", "0")
        upper = col2.text_input("Upper limit:", "pi")

    add_constant = st.checkbox(
        "Include constant of integration C (only for indefinite)",
        value=True
    ) if not definite else False
    simplify_res = st.checkbox("Simplify result", value=True)

    if st.button("Compute Integral"):
        with st.spinner("Computing..."):
            result = compute_integral(
                expr_str,
                var_str,
                lower,
                upper,
                definite,
                add_constant,
                simplify_res
            )
            if result is not None:
                st.subheader("Result")
                # Show LaTeX and plain text
                st.latex(sp.latex(result))
                st.write(f"Result: {result}")


if __name__ == "__main__":
    main()
