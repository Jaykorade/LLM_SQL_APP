import streamlit as st
import pandas as pd
import numpy as np


st.title("hello streamlit")

st.write('this is simple txt')

df = pd.DataFrame({'FIRST':[1,2,3,4],
                   '2ND':[1,2,4,3]
                   })


st.dataframe = df

st.write('it is dataframe')
st.write(df)

chart_data = pd.DataFrame(
    
        np.random.randn(20,3),columns=['a','b','c']
    
)

st.line_chart(chart_data)