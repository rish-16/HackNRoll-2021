from summarizer import Summarizer
from pprint import pprint

class BERTSummariser:
    def __init__(self):
        self.model = Summarizer()
        
    def predict(self, body):
        return self.model(body, ratio=0.4)

bert = BERTSummariser()
data = {}

with open("text/transcript3.txt") as f:
    body = f.read().strip().split("\n")
    body = [body[i].strip().split(" | ") for i in range(len(body))]
    
for i in range(len(body)):
    data[body[i][1]] = body[i][0]
    
text = ". ".join(list(data.keys()))
print (text)

preds = bert.predict(text)
print (preds)

with open("res/result3.txt", "a") as f:
    f.write("".join(preds))