import numpy as np
import pandas as pd

def data_split(dataset, target_string, X_feats_list):
    target = dataset[target_string]
    df_no_target = dataset.drop('successful_dummy', axis=1)
    X = pd.get_dummies(df_no_target[X_feats_list])
    return X, target
