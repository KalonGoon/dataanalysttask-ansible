import streamlit as st
import pandas as pd

st.title("Baby Names Popularity: 2007 vs 2020")

@st.cache_data
def load_data():
    return pd.read_csv("baby_names.csv")

data = load_data()

top_2007 = data[(data['Year'] == 2007) & (data['Rank'] <= 10)]
top_2020 = data[(data['Year'] == 2020) & (data['Rank'] <= 100)]

def dropped_names(gender):
    names_2007 = set(top_2007[top_2007['Gender'] == gender]['Name'])
    names_2020 = set(top_2020[top_2020['Gender'] == gender]['Name'])
    dropped = names_2007 - names_2020
    return dropped

male_dropped = dropped_names('M')
female_dropped = dropped_names('F')

st.subheader("Male Names Dropped from Top 100 (2007 Top 10 → 2020)")
for name in male_dropped:
    st.write(name)

st.subheader("Female Names Dropped from Top 100 (2007 Top 10 → 2020)")
for name in female_dropped:
    st.write(name)

st.write("""
- Filtered top 10 male and female baby names from 2007.
- Compared to top 100 names in 2020.
- Listed names that were top 10 in 2007 but fell outside the top 100 in 2020.
""")
