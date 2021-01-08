from data import get_data
from bert_qa import BERTQA

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
text = r"{}".format(text)

model = BERTQA(text)

preds = model.predict("What does research show about calming down?")
print (preds)

preds = model.predict("What is the problem with our brains?")
print (preds)