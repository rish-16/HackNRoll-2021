from pprint import pprint
import pandas as pd
from data import get_data
from bert_sum import BERTSummariser

bert = BERTSummariser()
hash_lookup = {}

df = get_data()

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

print (text)
preds = bert.predict(text)
print (preds)

# with open("res/result5.txt", "a") as f:
