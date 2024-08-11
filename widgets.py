import streamlit as st
import pandas as pd
import csv
st.title('streamlit text input')

name =st.text_input('enter your name:')


if name:
    st.write(f'hello,{name}')

age=st.slider('select your age:',0,100,25)
st.write(f"your age is {age}")

options=['python','java','ruby']
choice = st.selectbox(f"choose your fav options:",options)

st.write(f"you selected {choice}")


df = pd.DataFrame({'FIRST':[1,2,3,4],
                   '2ND':[1,2,4,3]
                   })

st.write(df)

uploaded_file = st.file_uploader("choose csv file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

