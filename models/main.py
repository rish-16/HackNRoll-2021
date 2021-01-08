from pprint import pprint
import pandas as pd
from data import get_data
from bert_sum import BERTSummariser

bert = BERTSummariser()

df = get_data()
df.to_csv("./data/source.csv")

sents = df['text']
hash_lookup = {}

text = ""
prev = ""
prev_row = None

for idx, row in df.iterrows():
    sent = row['text'].strip()

    if sent[-1] == "." or sent[-1] == "?" or sent[-1] == "!":
        prev += sent[:-1]
        hash_lookup[prev] = prev_row
        prev = ""
    else:
        prev += sent[:-1] + " "
        
    prev_row = {row['start'], row['end'], row['duration']}
        
text = " ".join(list(hash_lookup.keys()))

pprint (list(hash_lookup.keys())[:5])

preds = bert.predict(text)
proc_preds = preds.split("|")

print ()
pprint (proc_preds[:5])