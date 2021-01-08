from summarizer import Summarizer
from pprint import pprint

model = Summarizer()

data = {}

with open("transcript.txt") as f:
    body = f.read().strip().split("\n")
    body = [body[i].strip().split(" | ") for i in range(len(body))]
    
for i in range(len(body)):
    data[body[i][1]] = body[i][0]
    
text = "".join(list(data.values()))

preds = model(text, ratio=0.4)

with open("result.txt", "a") as f:
    f.write("".join(preds))