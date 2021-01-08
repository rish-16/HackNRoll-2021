import streamlit as st
from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_player import st_player

st.title('Video to Highlights')

st.subheader('Review Classification')
st.text_input('Youtube URL:')

st.text('Processing...')

# Video component
st_player('https://www.youtube.com/watch?v=-DP1i2ZU9gk')

# st.video()