import pandas as pd
import pickle

from utils.preprocess import cleaning

class ABSATourism:
    MODEL_PATH = '../model/model.pkl'
    VECTORIZER_PATH = '../model/vectorizer.pkl'
    LABEL = ['aksesibilitas', 'fasilitas', 'aktivitas']

    def __init__(self, text: str):
        self.object_model = open(self.MODEL_PATH, 'rb')
        self.model = pickle.load(self.object_model)
        self.vectorizer_model = open(self.VECTORIZER_PATH, 'rb')
        self.vectorizer = pickle.load(self.vectorizer_model)
        self.result = self.predict(text)

    def predict(self, text: str):
        text = cleaning(text)
        text = self.vectorizer.transform([text]) 
        text = pd.DataFrame(text.toarray(), columns=self.vectorizer.get_feature_names_out())

        probability = self.model.predict_proba(text)

        result = []

        for i in range(len(self.LABEL)):
            each_label = {'label': self.LABEL[i]}  #float("{:.3f}".format(probability[i]))
            each_label['score'] = {
                'neutral': float("{:.3f}".format(probability[i][0][0])),
                'positive': float("{:.3f}".format(probability[i][0][1])),
                'negative': float("{:.3f}".format(probability[i][0][2])),
            }
            result.append(each_label)

        return result