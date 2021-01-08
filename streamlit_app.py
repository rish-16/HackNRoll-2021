import streamlit as st
from pprint import pprint
import pandas as pd
from models.data import get_data
from models.bert_sum import BERTSummariser
from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_player import st_player
from fuzzywuzzy import fuzz


def init_model():
    bert = BERTSummariser()
    return bert

def preprocess_data(url):
    hash_lookup = {}
    df = get_data(url)

    raw_text = ""
    full_sent = ""
    first_timestamp = None

    for idx, row in df.iterrows():
        sent = row['text'].strip()

        if sent[-1] == "." or sent[-1] == "?" or sent[-1] == "!":
            full_sent += sent[:-1] + "."
            hash_lookup[full_sent] = first_timestamp
            # do something with full sentence and timestamp
            full_sent = ""
        else:
            full_sent += sent + " "
        
        first_timestamp = [row['start'], row['end'], row['duration']]
    # combine to form input paragraph
    text = " ".join(list(hash_lookup.keys()))
    return text


# st.image('sample.png', width=None)
# st.# %% [markdown]('Hello from SUM.ly')
st.markdown('# Hello from SUM.ly :wave:')
st.subheader('An interface where you can interact with as well as peek into your favorite videos.')

st.text("")
st.text("")

url = st.text_input('Enter the URL of your video')

if st.button('Pimp my video!'):
    with st.spinner("Please wait till we make your mind go brr........"):
        bert_model = init_model()
        transcript_text = preprocess_data(url)
        transcript_text_summary = bert_model.predict(transcript_text)
        st_player(url)
        st.write(transcript_text_summary)