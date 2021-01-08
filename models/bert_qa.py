from transformers import pipeline

class BERTQA:
    def __init__(self, context):
        self.context = context
        self.model = pipeline('question-answering')
        
    def predict(self, qn):
        return self.model(question=qn, context=self.context)['answer']
        
    