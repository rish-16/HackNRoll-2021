from pprint import pprint
import pandas as pd
from data import get_data
from bert_sum import BERTSummariser
from fuzzywuzzy import fuzz

bert = BERTSummariser()

URL = "https://www.youtube.com/watch?v=Hu4Yvq-g7_Y"
df = get_data(URL)

hash_lookup = {}

raw_text = ""
full_sent = ""
first_timesteamp = None

print ("Mapping")
for idx, row in df.iterrows():
    sent = row['text'].strip()

    if sent[-1] == "." or sent[-1] == "?" or sent[-1] == "!":
        full_sent += sent[:-1] + "."
        hash_lookup[full_sent] = first_timesteamp
        # do something with full sentence and timestamp
        full_sent = ""
    else:
        full_sent += sent + " "
    
    first_timesteamp = [row['start'], row['end'], row['duration']]
    
# combine to form input paragraph
text = " ".join(list(hash_lookup.keys()))

# split outputs by delimiter
print ("Prediction")
preds = bert.predict(text)
preds = preds.split(". ")

# query every sentence from output to get timestamp
res = []

print ("Comparison")
for sent, ts in hash_lookup.items():
    for ref_sent in preds:
        score = fuzz.ratio(sent, ref_sent)
        if score > 98:
            res.append([sent, ts])
            
print (res)