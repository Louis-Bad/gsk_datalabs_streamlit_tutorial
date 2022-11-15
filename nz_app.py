import streamlit as st
import pandas as pd

# Side bar
with st.sidebar:
    st.header("This is my sidebar baby!")

    select_box = st.selectbox(
        "This is my select box",
        ("Choice 1", "Choice 2", "Choice 3")
    )

    st.write("You have chosen", select_box)



    multi_select = st.multiselect(
        "This is the multi select",
        ["Female", "Male"]
    )



file_uplaod = st.file_uploader("upload file", type=["csv"])

@st.cache
def load_data(input, sep)


# if file_uplaod:
#     st.write("Nice that uploaded")
#     df = pd.read(file_uplaod)
# else:
#     st.write("still waiting for the file mate")

# st.write(df)