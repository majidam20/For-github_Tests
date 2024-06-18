### Import Libraries
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import sys
import gc
import random
import time
import pandas as pd
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(threshold=np.inf)

os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(42)
random.seed(12345)

###Start sklearn

from sklearn.model_selection import train_test_split


from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression


### End sklearn

###***Start tensorflow.keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, Dropout
from tensorflow.keras import optimizers
tf.random.set_seed(1234)

###**** End tensorflow.keras
import warnings
warnings.filterwarnings("ignore")


####End of importing libraries
from pathlib import Path
pathCurrrent = Path.cwd()


pathCurrrent = str(pathCurrrent).replace("\\", '/')


pathData = pathCurrrent + "/data/"

dfIncom = pd.read_csv(pathData+"income_data.csv", header=None)

dfEval = pd.read_csv(pathData+"eval.csv", header=None)

dfIncom=dfIncom.dropna()
dfEval=dfEval.dropna()


dfIncom=dfIncom.values
dfEval=dfEval.values

dfIncom=dfIncom[1:,:]
dfEval=dfEval[1:,3:]

dfEval[np.where(dfEval[:,:]=='> 5.800')]='5801'

dfIncom= dfIncom.astype('float64')
dfEval= dfEval.astype('int32')

datestr = time.strftime("%y%m%d_%H%M%S")
print(f"Start running time: {datestr},******************************:")


finalTestPercentage = 0.2
npTrain, npTest = train_test_split(, test_size=finalTestPercentage, random_state=42,shuffle=False)

npTrain[:,0]= npTrain[:,0].astype('int32')
npTrain[:,1]= npTrain[:,1].astype('float32')

npTest[:,0]=  npTest[:,0].astype('int32')
npTest[:,1]=  npTest[:,1].astype('float32')


npxTrain, npyTrain = npTrain[:,0], npTrain[:,1]
npxTest, npyTest = npTest[:,0], npTest[:,1]

npxTrain=npxTrain.reshape(-1,1)
npyTrain=npyTrain.reshape(-1,1)

npxTest=npxTest.reshape(-1,1)
npyTest=npyTest.reshape(-1,1)



###****Define Hyperparameters
epochs= 10
batch = 32
lr = 0.0001

model = Sequential()

  ### tanh, relu
model.add(Dense(512, activation='tanh' ))
model.add(Dense(512, activation='tanh' ))
model.add(Dense(128, activation='tanh' ))
model.add(Dense(64, activation='tanh' ))


model.add(Dense(1, activation='relu'))


adam = optimizers.Adam(lr)


model.compile(optimizer=adam, loss='mae', metrics=['mse'])


print("\n finalTest Model.summary(): \n")
print(model.summary())

print(f"\n finalTest Model config:\n {str(model.get_config())} \n\n")



history1 = model.fit(npxTrain.astype(int), npyTrain.astype(float), batch_size=batch, epochs=epochs
                                  , verbose=1, use_multiprocessing=True,
                                  shuffle=False).history

# X, y = make_regression(n_features=4, n_informative=2,
# random_state=0, shuffle=False)
# regr = RandomForestRegressor(max_depth=2, random_state=0)
# regr.fit(X, y)



print(f"\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$: \n")
print(f"---*** Average's Results of Model Evaluation is such as below: \n")

preds=model.predict(npxTest.astype(int))

print(f"Result error (revenue): {preds.mean()}")




