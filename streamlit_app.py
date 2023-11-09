# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:32:58 2023

@author: jhkim
"""

import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    
    
# Day 5
st.header('st.write')

# Example 1
st.write('Hello, *world!* :sunglasses:')

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)

# Example 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)