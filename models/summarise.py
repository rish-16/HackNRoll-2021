from summarizer import Summarizer
from pprint import pprint
import pandas as pd

class BERTSummariser:
    def __init__(self):
        self.model = Summarizer()
        
    def predict(self, body):
        return self.model(body, ratio=0.4)

bert = BERTSummariser()
data = {}

df = None
sents = df['sentence']
text = "".join(sents)
    
preds = bert.predict(text)

with open("res/result3.txt", "a") as f:
    f.write("".join(preds))