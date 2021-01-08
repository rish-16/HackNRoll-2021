from summarizer import Summarizer

class BERTSummariser:
    def __init__(self):
        self.model = Summarizer()
        
    def predict(self, body):
        return self.model(body, ratio=0.2)