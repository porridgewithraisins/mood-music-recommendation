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


pip = Pipeline([('minmaxscaler',MinMaxScaler()),('keras',classifier)])
pip.fit(X2,y_label)

def predict_mood(song_features):
    
    features = np.array(song_features).reshape(-1,1).T
    result = pip.predict(features)
    mood = np.array(labels['mood'][labels['label']==int(result)])

    return mood[0]
