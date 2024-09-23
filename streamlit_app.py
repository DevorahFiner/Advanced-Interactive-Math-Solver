import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Advanced Interactive Math Solver")
st.write("Solve equations, compute derivatives, or evaluate integrals with visualizations!")

# Sidebar for choosing operation
operation = st.sidebar.selectbox(
    "Choose the operation:",
    options=["Solve Quadratic Equation", "Find Derivative", "Evaluate Integral"]
)

x = sp.symbols('x')

# Solve Quadratic Equation
if operation == "Solve Quadratic Equation":
    st.header("Solve Quadratic Equation")
    a = st.number_input("Enter coefficient a:", value=1)
    b = st.number_input("Enter coefficient b:", value=0)
    c = st.number_input("Enter coefficient c:", value=0)

    if st.button("Solve"):
        equation = sp.Eq(a*x**2 + b*x + c, 0)
        solutions = sp.solve(equation, x)
        st.write(f"Solutions: {solutions}")

        # Optionally plot the quadratic function
        if st.checkbox("Plot the quadratic function?"):
            x_vals = np.linspace(-10, 10, 400)
            y_vals = a * x_vals ** 2 + b * x_vals + c
            plt.plot(x_vals, y_vals)
            plt.axhline(0, color='gray', lw=0.5, ls='--')
            plt.axvline(0, color='gray', lw=0.5, ls='--')
            plt.title(f"Quadratic Function: {a}x² + {b}x + {c}")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            st.pyplot(plt)

# Find Derivative
elif operation == "Find Derivative":
    st.header("Find Derivative")
    expression = st.text_input("Enter a mathematical expression:")
    
    if expression:
        expr = sp.sympify(expression)
        derivative = sp.diff(expr, x)
        st.write(f"The derivative of {expression} is:")
        st.latex(sp.latex(derivative))

        # Plot the function and its derivative
        if st.checkbox("Plot the function and its derivative?"):
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [expr.evalf(subs={x: val}) for val in x_vals]
            y_derivative_vals = [derivative.evalf(subs={x: val}) for val in x_vals]
            plt.plot(x_vals, y_vals, label='Function')
            plt.plot(x_vals, y_derivative_vals, label='Derivative', linestyle='--')
            plt.axhline(0, color='gray', lw=0.5, ls='--')
            plt.axvline(0, color='gray', lw=0.5, ls='--')
            plt.title("Function and its Derivative")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            st.pyplot(plt)

# Evaluate Integral
elif operation == "Evaluate Integral":
    st.header("Evaluate Integral")
    expression = st.text_input("Enter a mathematical expression to integrate:")
    
    if expression:
        expr = sp.sympify(expression)
        integral = sp.integrate(expr, x)
        st.write(f"The integral of {expression} is:")
        st.latex(sp.latex(integral))

        # Plot the integral area
        if st.checkbox("Plot the integral area?"):
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [expr.evalf(subs={x: val}) for val in x_vals]
            plt.fill_between(x_vals, y_vals, where=(y_vals > 0), alpha=0.3, label='Area under the curve')
            plt.axhline(0, color='gray', lw=0.5, ls='--')
            plt.axvline(0, color='gray', lw=0.5, ls='--')
            plt.title("Area Under the Curve")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.legend()
            st.pyplot(plt)
