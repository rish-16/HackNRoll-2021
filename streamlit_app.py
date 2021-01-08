import streamlit as st
from pprint import pprint
import pandas as pd
from models.data import get_data
from models.bert_sum import BERTSummariser

def init_model():
    bert = BERTSummariser()
    return bert

# @st.cache()
def preprocess_data(url):
    hash_lookup = {}
    df = get_data(url)

    sents = df['text']
    text = ""
    prev = ""
    prev_row = None

    for idx, row in df.iterrows():
        if "." in row['text']:
            prev += " " + row['text']
            hash_lookup[prev] = prev_row
            prev = ""
            prev_row = {row['start'], row['end'], row['duration']}
        else:
            prev += " " + row['text']
            prev_row = {row['start'], row['end'], row['duration']}
            
    text = "".join(list(hash_lookup.keys()))
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
        bert_model = BERTSummariser()
        transcript_text = preprocess_data(url)
        transcript_text_summary = bert_model.predict(transcript_text)
        st.write(transcript_text_summary)