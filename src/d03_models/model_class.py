import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV

class modelSelection:
    def __init__(self, algorithm, dataset, target_variable):
        self.y = dataset['successful_dummy']
        self.df_no_y = dataset.drop('successful_dummy', axis=1)
        self.X_feats = ['category', 'blurb_word_count', 'campaign_length',
                   'delta_created_launched', 'goal_usd','world_regions',
                   'cluster_predictions']
        self.X = pd.get_dummies(df_no_y[X_feats])
        self.algorithm = algorithm
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, stratify=y)

    def fit(X_train, y_train):
        self.algorithm.fit(X_train, y_train)

    def predict(X_test):
        self.y_pred = self.algorithm.predict(X_test)

    def accuracy(x):
        self.accuracy = accuracy_score(y_test, y_pred)
        return self.accuracy
