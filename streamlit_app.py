# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:32:58 2023

@author: jhkim
"""

import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime

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

# Day 8
st.header('st.slider')

# Example 1
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2
st.subheader('Range slider')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3
st.subheader('Range time slider')

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12,45)))
st.write("You're scheduled for:", appointment)

# Example 4 
st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


# Day 9
st.header('Line Chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Day 10
st.header('st.selectbox')
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)


# Day 11
st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)


# Day 12
st.header('st.checkbox')
st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more :icecream:")
if coffee:
    st.write("Okay, here's some :coffee:")
if cola:
    st.write("Here you go :cola:")

# Day 15
st.header('st.latex')

st.latex(r'''
         a + ar + a r^2 +a r^3 + \cdots +a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)
         ''')

# Day 16
#st.title('Customizing the theme of Streamlit apps')

#st.write('Contents of the '/config.toml' file of this app')

#st.code("""
#[theme]
#primaryColor="#F39C12"
#backgroundColor="#2E86C1"
#secondaryBackgroundColor="#AED6F1"
#textColor="#FFFFFF"
#font="monospace"
#""")

#number = st.sidebar.slider('Select a number:', 0, 10, 5)
#st.write('Selected number from slider widget is:', number)


# Day 17
#st.title('st.secrets')
#st.write(st.secrets['message'])


# Day 18
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('Upload a CSV file')


# Day 19
#st.set_page_config(layout="wide")
#st.title('How to layout your Streamlit app')

#with st.expander('About this app'):
#    st.write('This app shows the various ways on how you can layout your Streamlit app.')
#    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
#st.sidebar.header('Input')
#user_name = st.sidebar.text_input('What is your name?')
#user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
#user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

#st.header('Output')

#col1, col2, col3 = st.columns(3)

#with col1:
#    if user_name != '':
#        st.write(f'👋 Hello {user_name}!')
#    else:
#        st.write('👈  Please enter your **name**!')
#with col2:
#    if user_emoji != '':
#        st.write(f'{user_emoji} is your favorite **emoji**!')
#    else:
#        st.write('👈 Please choose an **emoji**!')

#with col3:
#    if user_food != '':
#        st.write(f'🍴 **{user_food}** is your favorite **food**!')
#    else:
#        st.write('👈 Please choose your favorite **food**!')


# Day 21
import time

st.title('st.progress')
with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()


# Day 22
st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


# Day 23
st.title('st.experimental_get_query_params')

with st.expander('About this app'):
  st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.experimental_get_query_params())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

#firstname = st.experimental_get_query_params()['firstname'][0]
#surname = st.experimental_get_query_params()['surname'][0]

#st.write(f'Hello **{firstname} {surname}**, how are you?')


# Day 24
from time import time
st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df
st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)


# Day 25
#st.title('st.session_state')

#def lbs_to_kg():
#    st.session_state.kg = st.session_state.lbs/2.2046
#def kg_to_lbs():
#    st.session_state.lbs = st.session_state.kg*2.2046

#st.header('Input')
#col1, spacer, col2 = st.solumns([2, 1, 2])
#with col1:
#    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
#with col2:
#    kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

#st.header('Output')
#st.write("st.session_state object:", st.session_state)


# Day 26
import requests

st.title('Bored API app')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
    with st.expander('About this app'):
        st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')
