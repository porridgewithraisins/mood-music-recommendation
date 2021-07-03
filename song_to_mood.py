#PREPROCESSING

import numpy as np 
import pandas as pd 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_v2_behavior()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.pipeline import Pipeline


df = pd.read_csv("moods.csv")
mood_features = df.columns[6:-3]
X= MinMaxScaler().fit_transform(df[mood_features])
X2 = np.array(df[mood_features])
Y = df['mood']

encoder = LabelEncoder()
encoder.fit(Y)
y_label = encoder.transform(Y)

# X_train,X_test,Y_train,Y_test = train_test_split(X,y_label,test_size=0.2,random_state=15)
# TEST ACCURACY : 87%

labels = pd.DataFrame({'mood':df['mood'].tolist(),'label':y_label}).drop_duplicates().sort_values(['label'],ascending=True)
def model():

    _model = Sequential()
    _model.add(Dense(8,input_dim=10,activation='relu'))
    _model.add(Dense(4,activation='softmax'))
    _model.compile(loss='categorical_crossentropy',optimizer='adam',
                 metrics=['accuracy'])
    return _model

classifier = KerasClassifier(build_fn=model,epochs=300,
batch_size=200,verbose=0)

#gets mood features of song id from tracks.csv
#TODO
def get_mood_features(song_id):
    #something big
    
    l = [161440,0.694,0.00614,0.854,0,0.158,0.803,-3.891,0.043,112.007]
    #1999
    l1 = [379266,0.866,0.13699999999999998,0.73,0,0.0843,0.625,-8.201,0.0767,118.523]

    #holding me back
    l2 = [199440,0.866,0.38,0.813,0,0.0779,0.969,-4.063,0.0554,121.998]
    #all of me
    l3 = [269560,0.422,0.922,0.264,0,0.132,0.331,-7.064,0.0322,119.93]
    #bloom
    l4 = [121069,0.249,0.945,0.129,0.8390000000000001,0.17,0.253,-18.167,0.0324,70.59]
    
    return l4


pip = Pipeline([('minmaxscaler',MinMaxScaler()),('keras',classifier)])
pip.fit(X2,y_label)

def predict_mood(song_features):
    
    features = np.array(song_features).reshape(-1,1).T
    result = pip.predict(features)
    mood = np.array(labels['mood'][labels['label']==int(result)])

    return mood[0]
