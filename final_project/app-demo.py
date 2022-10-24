import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Haobo Yang')

data = {
    'name': ['tom', 'jerry', 'mary'],
    'gender':['male', 'male', 'female'],
    'age':[22, 25, 23]

}

df = pd.DataFrame(data)

st.write(df)
