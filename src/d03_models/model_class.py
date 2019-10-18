import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

class modelSelection:
    def __init__(self, algorithm, algorithm_name, X, y):
        self.algorithm = algorithm
        self.X = X
        self.y = y
        self.algorithm_name = algorithm_name

    def train_test_split_func(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, stratify=self.y, random_state=88)

    def fit_func(self):
        self.algorithm.fit(self.X_train, self.y_train)

    def predict_func(self):
        self.prediction = self.algorithm.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.prediction)
        self.precision = precision_score(self.y_test, self.prediction)
        self.recall = recall_score(self.y_test, self.prediction)
        self.confusion_matrix = pd.DataFrame(confusion_matrix(self.y_test, self.prediction),
                     index = ['actual 0', 'actual 1'],
                     columns = ['predicted 0', 'predicted 1'])

    def model_evaluation(self):
        print('Acccuracy Score: ', self.accuracy)
        print('Precision: ', self.precision)
        print('Recall: ', self.recall)
        print('\n')
        print('Confusion Matrix:')
        print(self.confusion_matrix)
