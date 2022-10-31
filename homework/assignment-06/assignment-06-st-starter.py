# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# show the title
st.title('Titanic App by Haobo Yang')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
st.dataframe(df)
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1,3, figsize=(15,5))
fare_1 = df[df.Pclass == 1]
fare_2 = df[df.Pclass == 2]
fare_3 = df[df.Pclass == 3]
fare_1.Fare.plot.box(ax = ax[0])
fare_2.Fare.plot.box(ax = ax[1])
fare_3.Fare.plot.box(ax = ax[2])

ax[0].set_ylabel('Fare')
ax[0].set_xlabel('PClass = 1')
ax[1].set_xlabel('PClass = 2')
ax[2].set_xlabel('PClass = 3')

st.pyplot(fig)
