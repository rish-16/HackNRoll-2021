import streamlit as st
from pprint import pprint
import pandas as pd
from models.data import get_data
from models.bert_sum import BERTSummariser
from models.bert_qa import BERTQA
from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_player import st_player
from fuzzywuzzy import fuzz


hash_lookup = {}


def init_model():
    bert_summarizer = BERTSummariser()
    return bert_summarizer

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

@st.cache
def get_summary(bert_summarizer, transcript_text):
    return bert_summarizer.predict(transcript_text)
# st.image('sample.png', width=None)
# st.# %% [markdown]('Hello from SUM.ly')
st.markdown('# Hello from SUM.ly :wave:')
st.subheader('An interface where you can interact with as well as peek into your favorite videos.')

st.text("")
st.text("")

url = st.text_input('Enter the URL of your video')

transcript_text_summary=""
transcript_text = preprocess_data(url)
bert_summarizer = init_model()

st.text("")
st.text("")

st.header('Video Highlights')
if st.button('Pimp my video!'):
    with st.spinner("Please wait till we make your mind go berrrrttt........"):

        transcript_text_summary = get_summary(bert_summarizer, transcript_text)
        ranges = map_preds_to_ranges(transcript_text_summary)
        st_player(url, ranges=ranges)

transcript_text_summary = get_summary(bert_summarizer, transcript_text)
st.subheader("Video Summary")
st.write(transcript_text_summary)

st.header('Live Query : Ask me Anything')

user_question = st.text_input("What do you want know today ?")

if st.button("Quiz me! I'm Ready"):
    bert_qa = BERTQA(transcript_text)
    answer = bert_qa.predict(user_question)
    st.write("I think it is " + answer)

