import openai
import streamlit as st

import datetime

import os

openai.api_key = st.secrets["apiSecret"]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are wise, loving, positive, and warm. Your role is to offer concise pearls of wisdom. You write in the style of Jenny Slate and David Sedaris. Your responses are up to 3 sentences long. Provide wisdom on one topic only. Be quirky, whimsical, funny, and endearing."},
      {"role": "user", "content": "Offer some concise wisdom on a random important topic related to living well and wisely. Avoid using ther phrase: on the topic of"}
  ],
  temperature=0.9,
  max_tokens=128,
)

# create and initiatlize app hit counter
if 'hitCount' not in st.session_state:
    st.session_state.hitCount = 0

# increment app hit count
#st.session_state.hitCount += 1

#implement some kind of website hit counter
#https://www.geeksforgeeks.org/python-count-number-of-hits-on-a-particular-url-using-flask/

# Create a Streamlit app
st.title("Welcome, digital wanderer!")
st.write("This is an experimental sandbox.")
st.write("\nDaily nugget of wisdom:")

# Generate a random text
st.write(response["choices"][0]["message"]["content"])

# generate a new response every 24 hours
#https://discuss.streamlit.io/t/how-to-run-a-function-every-24-hours/1809/2

increment = st.button('Please sir, I want some more!')

if increment:
    st.session_state.hitCount += 1

st.write("\n", st.session_state.hitCount,"served")




