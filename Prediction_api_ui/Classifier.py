import os
import joblib

class MyClassifier:

    def __init__(self):
        self.model = None

    def predict(self,list1):
        model_name = os.environ.get('MODEL_NAME', 'Specified environment variable is not set.')
        if self.model is None:
            self.model = joblib.load(model_name)
        X1=[list1]
        prediction = self.model.predict(X1)
        # print('Predictin is ')
        # print(predictions)
        return  prediction