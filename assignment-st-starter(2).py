# import packages
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# show the title
st.title('Titanic App by Jiachen Zheng')

# read csv and show the dataframe
df_train= pd.read_csv('train.csv')
df_train



# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
First_class = df_train[df_train['Pclass'] == 1]['Fare']
Second_class = df_train[df_train['Pclass'] == 2]['Fare']
Third_class = df_train[df_train['Pclass'] == 3]['Fare']
axs[0].boxplot(First_class)
axs[0].set_xlabel('PClass=1')
axs[0].set_ylabel('Fare')
axs[1].boxplot(Second_class)
axs[1].set_xlabel('PClass=2')
axs[1].set_ylabel('Fare')
axs[2].boxplot(Third_class)
axs[2].set_xlabel('PClass=3')
axs[2].set_ylabel('Fare')
plt.tight_layout()
plt.show()
