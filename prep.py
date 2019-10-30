import pandas as pd
import numpy as np

def basic_clean(df):
	df.total_charges = df.total_charges.str.strip().replace('', np.nan).astype(float)
	df = df.set_index("customer_id")
	df.fillna(np.nan, inplace=True)
	df = df.dropna()
	return df

def split_my_data(data):
	from sklearn.model_selection import train_test_split
	return train_test_split(data, train_size = 0.8, random_state = 123)

def new_feature(train, test):

	train, test = encode(train, test, "online_security")
	train, test = encode(train, test, "online_backup")
	train, test = encode(train, test, "device_protection")
	train, test = encode(train, test, "tech_support")
	train, test = encode(train, test, "partner")
	train, test = encode(train, test, "dependents")
	train, test = encode(train, test, "streaming_tv")
	train, test = encode(train, test, "streaming_movies")

	train['online_add_on'] = (train.online_security == True) | (train.online_backup == True)
	train['online_add_on'] = (test.online_security == True) | (test.online_backup == True)

	train['support'] = (train.device_protection == 2) | (train.tech_support == 2)
	test['support'] = (test.device_protection == 2) | (test.tech_support == 2)

	train['family'] = (train.partner == True) | (train.dependents == True)
	test['family'] = (test.partner == True) | (test.dependents == True)

	train['streaming_pack'] = (train.streaming_tv == 2) | (train.streaming_movies == 2)
	test['streaming_pack'] = (test.streaming_tv == 2 ) | (test.streaming_movies == 2)

	train, test = prep.encode(train, test, "online_add_on")
	train, test = prep.encode(train, test, "support")
	train, test = prep.encode(train, test, "family")
	train, test = prep.encode(train, test, "streaming_pack")
	
	return train, test

def encode(train, test, col_name):
    from sklearn.preprocessing import LabelEncoder
    
    # Integer Encoding
    int_encoder = LabelEncoder()
    train[col_name] = int_encoder.fit_transform(train[col_name])
    test[col_name] = int_encoder.transform(test[col_name])
    
    return train, test
