import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline




class Analyse:
    tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
    model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")
    emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
    count = 1
    
    def __init__(self) -> None:
        pass
       
    def reduce(self, text):
        reducedTextArray = text.split(" ")[:200]
        reducedText = ""
        for word in reducedTextArray:
            reducedText += word+" "
        return reducedText

    def classify(self, text):
        print("Article: "+str(self.count))
        self.count += 1
        return self.emotion(text)[0]['label']

    def runAnalyse(self,):
        df = pd.read_csv('./data/results/scrapeddata.csv')
        df['reduced'] = df['Content'].apply(self.reduce)
        df['Emotion'] = df['reduced'].apply(self.classify)
        sns.countplot(data = df, y = 'Emotion').set_title("Emotion Distribution")
        plt.savefig('./data/results/plot.png')
        df = df.iloc[: , -2: ]
        df.to_csv('./data/results/emotions.csv')

