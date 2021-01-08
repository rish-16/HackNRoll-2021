import streamlit as st
from pprint import pprint
import pandas as pd
from models.data import get_data
from models.bert_sum import BERTSummariser
from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_player import st_player
from fuzzywuzzy import fuzz


hash_lookup = {}


def init_model():
    bert = BERTSummariser()
    return bert

def preprocess_data(url):
    df = get_data(url)

    raw_text = ""
    full_sent = ""
    first_timestamp = None

    for idx, row in df.iterrows():
        sent = row['text'].strip()

        # if first row in sentence
        if full_sent == "":
            start = row['start']

        if sent[-1] == "." or sent[-1] == "?" or sent[-1] == "!":
            full_sent += sent[:-1] + "."
            hash_lookup[full_sent] = {
                'start': start,
                'end': row['end']
            }
            # do something with full sentence and timestamp
            full_sent = ""
        else:
            full_sent += sent + " "
    # combine to form input paragraph
    text = " ".join(list(hash_lookup.keys()))
    return text

def map_preds_to_ranges(preds):
    preds = preds.split(". ")
    # query every sentence from output to get timestamp
    res = []

    print ("Comparison")
    for sent, ts in hash_lookup.items():
        for ref_sent in preds:
            score = fuzz.ratio(sent, ref_sent)
            if score > 98:
                res.append({
                    'start': ts['start'],
                    'end': ts['end'],
                })
    return res



# st.image('sample.png', width=None)
# st.# %% [markdown]('Hello from SUM.ly')
st.markdown('# Hello from SUM.ly :wave:')
st.subheader('An interface where you can interact with as well as peek into your favorite videos.')

st.text("")
st.text("")

url = st.text_input('Enter the URL of your video')

transcript_text_summary=""

if st.button('Pimp my video!'):
    with st.spinner("Please wait till we make your mind go brr........"):
        bert_model = init_model()
        transcript_text = preprocess_data(url)
        transcript_text_summary = bert_model.predict(transcript_text)

        ranges = map_preds_to_ranges(transcript_text_summary)
        st_player(url, ranges=ranges)
        st.write(transcript_text_summary)

        st.text_input(":magnifying_glass: Enter your question for QA Model here")
        st_player(url)
        st.write(transcript_text_summary)
        # st.markdown(
        #     """
        #     <style>
        #     .body {
        #         height:500px;
        #         overflow:scroll
        #     }
        #     </style>
        #     <div class='body'>{}</div>
        #     """.format(transcript_text_summary)
        #     ,
        #     unsafe_allow_html=True,
        # )


