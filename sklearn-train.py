#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib


def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf



if __name__ =='__main__':
    
    print("HI")

    parser = argparse.ArgumentParser()
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--train-file', type = str, default='df_train.csv')
    parser.add_argument('--min_samples_leaf', type = str, default=1)
    parser.add_argument('--min_samples_split', type = str, default=20)
    parser.add_argument('--target', type = str) 

    args, _ = parser.parse_known_args()

    print('reading data')
    train_df = pd.read_csv(os.path.join(args.train, args.train_file))
    
    features = np.setdiff1d(train_df.columns,args.target )
    
    print('building training datasets')
    X_train = train_df[features]
    y_train = train_df[args.target]

    # train
    print('training model')
    print(args.min_samples_leaf)
    model = RandomForestRegressor(min_samples_split = 20)
     
    print(X_train.head())    
    print(y_train.head())
    model.fit(X_train, y_train)
     
    # persist model
    path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, path)
    print('model persisted at ' + path)

