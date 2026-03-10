import streamlit as st
import pandas as pd
import numpy as np

###
st.set_page_config(page_title="Streamlit App 05_PSP01 Module 1",layout='centered')
st.title("Streamlit App 05_PSP01 Module 1")
st.caption("A simple Streamlit app to demonstrate some of its capabilities.")

###
st.header("Weather in European cities dataset")
df = pd.DataFrame({
    "city":["Paris","London","Berlin","Stockholm"],
    "temp": [24,20,21,18],
    "rain":[False,True,True,True]
})
show_raw=st.checkbox("Show raw data", value=False)
if not show_raw:
    st.subheader("Bar chart for weather data")
    st.bar_chart(df, x='city', y='temp', color='rain')
else:
    st.subheader("Raw data for weather data")
    st.dataframe(df, use_container_width=True)

###
st.header("Line chart for random data")
chart_df=pd.DataFrame(np.random.randn(20,3), columns=list('ABC'))
st.line_chart(chart_df)

###
with st.sidebar:
    st.header("Settings")
    theme=st.selectbox("Theme", ["Light","Dark","Auto"], index=0)

###
st.header("User Information")
col1,col2=st.columns(2)
with col1:
    name=st.text_input("Your name",placeholder="Enter Name")
with col2:
    age=st.slider("Select your age", min_value=1, max_value=100, value=50)
st.write(f"Name: {name}")
st.write(f"Age: {age}")
langs=["Python","Java","Angular","TypeScript"]
primary_lang=st.selectbox("Primary language", langs, index=1)
experience_level=st.radio("Primary language experience level", ["Beginner", "Intermediate", "Expert"], index=2, horizontal=False)
other_langs = langs.copy()
other_langs.remove(primary_lang)
other_langs_select=st.multiselect("Other languages", other_langs, default=other_langs[0])

###
with st.form("user_info_form"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Primary language: {primary_lang}")
    st.write(f"Primary language experience level: {experience_level}")
    if other_langs_select:
        st.write("Other languages:", ", ".join(other_langs_select))
    else:
        st.write("Other languages: None")
    enjoy_st = st.checkbox("Enjoying Streamlit?", value=True)
    hours_st = st.number_input("Hours spent on Streamlit", min_value=1, max_value=40, value=10)
    submitted = st.form_submit_button("Submit")

###
if submitted:
    summary_df = pd.DataFrame({
        "Field": [
            "Name",
            "Age",
            "Primary language",
            "Experience level",
            "Other languages",
            "Enjoying Streamlit",
            "Hours spent on Streamlit",
        ],
        "Value": [
            name,
            age,
            primary_lang,
            experience_level,
            ", ".join(other_langs_select) if other_langs_select else "None",
            enjoy_st,
            hours_st,
        ],
    })
    st.subheader("Submitted Information")
    st.dataframe(summary_df, hide_index=True, use_container_width=True)