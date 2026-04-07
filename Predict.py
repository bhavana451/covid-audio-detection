import os
import pandas as pd
import numpy as np
import csv
from pydub import AudioSegment 
import librosa
import glob
from sklearn.linear_model import LogisticRegression
from tensorflow.keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation ,Dropout , Flatten , Conv1D ,MaxPooling1D
from keras.layers.recurrent import LSTM

SAMPLE_RATE = 44100
#returns mfcc features with mean and standard deviation along time
def get_mfcc(path):
    b, _ = librosa.core.load(path, sr = SAMPLE_RATE)
    assert _ == SAMPLE_RATE
    try:
        gmm = librosa.feature.mfcc(b, sr = SAMPLE_RATE, n_mfcc=20)
        print(gmm)
        spectral_centroids = librosa.feature.spectral_centroid(b, sr=SAMPLE_RATE)[0]
        print("-------------")
        print(spectral_centroids)
        return pd.Series(np.hstack((np.mean(gmm, axis=1), np.std(gmm, axis=1))))
    except:
        print('bad file')
        return pd.Series([0]*40)

def process(path):
	mfcc=[]
	amount_of_features=40
	s=get_mfcc(path)
	print(s.tolist())
	mfcc.append(s.tolist())
	full=[]
	for i in range(0,len(mfcc)):
		print(mfcc[i])
		d=[]
		for j in mfcc[i]:
			print(j)
			d.append(j)
		full.append(d)
	print(full)
	df = pd.read_csv("dataset.csv")
	X_train = df.iloc[ : , :-1].values
	y_train = df.iloc[:, -1:].values
	X_test=full
	model = load_model("results/CNNLSTM.h5")
	model2=LogisticRegression(random_state = 0)
	model2.fit(X_train, y_train)
	y_pred = model2.predict(X_test)
	print("predicted")
	print(y_pred)
	result=""
	if y_pred[0]==0:
		result="Non-Covid"
	elif y_pred[0]==1:
            result="Covid+ve"
            
	else:
		result="Normal"
	return result
	
	
#process("./Dataset/Noncovid/1745-9974-2-1-S1.wav")
