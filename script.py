import pickle
import pandas as pd
import json
import sys


model = None

pickle_file = 'trained_model.pkl' 
with open (pickle_file, 'rb') as file:
    model = pickle.load(file)

def run_model(): 
    data = sys.argv[1]
    df = pd.DataFrame(data, columns=['homeworld', 'unit_type'])
    df_encoded = pd.get_dummies(df)
    predictions = model.predict(df_encoded)
    predictions_json = json.dumps(predictions)
    return predictions_json