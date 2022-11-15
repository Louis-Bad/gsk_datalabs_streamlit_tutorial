""" In this demo, we explore some components of Streamlit.

To run the application: $ streamlit run streamlit_intro.py

Users are encouraged to play with the code and observe the consequences
of their changes in the web app (http://localhost:8501).

Have fun!
"""

import inspect
import textwrap
from datetime import datetime, time

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

##########################
# PART 1
##########################
st.title("Day 10")
st.write("Hello DataLabs! Let's have a look at some of the components together.")

st.markdown("""---""")
##########################
# PART 2 sidebar and button
##########################
with st.sidebar:
    st.header("st.button")

    if st.button("Say hello Streamlit"):
        st.write("Howdie")
    else:
        st.write("Bye bye now")

    st.markdown("""---""")
##########################
# PART 3 write
##########################
st.header("st.write")

# Example 1

st.write("Hello, *DataLabs!* :sunglasses:")

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

# Example 4

st.write("Below is a DataFrame:", df, "Above is a dataframe.")

# Example 5

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(c)

# Example with Latex
st.latex(
    r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    """
)

# Example with code
def print_source_code():
    st.markdown("## Code")
    sourcelines, _ = inspect.getsourcelines(print_source_code)
    st.code(textwrap.dedent("".join(sourcelines[1:])))


print_source_code()
st.markdown("""---""")
##########################
# PART 4 slider
##########################
st.header("st.slider")

# Example 1

st.subheader("Slider")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

# Example 2

st.subheader("Range slider")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

# Example 3

st.subheader("Range time slider")

appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader("Datetime slider")

start_time = st.slider(
    "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)
st.markdown("""---""")
##########################
# PART 5 line chart
##########################
st.header("Line chart")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
st.markdown("""---""")
##########################
# PART 6 selectbox
##########################
st.header("st.selectbox")

option = st.selectbox(
    "What is your department?", ("Finance", "Research", "Development")
)

st.write("Your department is ", option)


st.header("st.multiselect")

options = st.multiselect(
    "What are your departments?",
    ["Finance", "Research", "Development", "HR"],
    ["Research", "Development"],
)

st.write("You selected:", options)

st.markdown("""---""")
##########################
# PART 7 checkbox
##########################
st.header("st.checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")
st.markdown("""---""")
