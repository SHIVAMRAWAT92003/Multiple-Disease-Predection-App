# -*- coding: utf-8 -*-
"""DiabetesPrediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vp23nkuUyFBD_uktnkAKa7ZELS0Jgmd3

IMPORTING DEPENDENCIES
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""DATA COLLECTION AND ANALYSIS

"""

#loading diabetes dataset to a pandas dataframe
diabetes_dataset=pd.read_csv('/content/diabetes.csv')

pd.read_csv?

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

#seperating the data and label
x=diabetes_dataset.drop(columns='Outcome',axis=1)
y=diabetes_dataset['Outcome']

print(x)

print(y)

#data standardization
scaler =StandardScaler()

scaler.fit(x)

Standardized_data=scaler.transform(x)

#data standardization
scaler =StandardScaler()
scaler.fit(x) # Fit the scaler to the data 'x'
Standardized_data=scaler.transform(x) # Transform the data using the fitted scaler

print(Standardized_data)

x=Standardized_data
y=diabetes_dataset['Outcome']

print(x)
print(y)

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

(x.shape,X_train.shape,X_test.shape)

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

#accuracy score on the training data
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the trainig data: ',training_data_accuracy)

#accuracy score on the testing data
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of the trainig data: ',test_data_accuracy)

"""MAKING A PREDICTIVE SYSTEM"""

input_data=(4,110,92,0,0,37.6,0.191,30)


input_data_as_numpy_array = np.asarray(input_data)


input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)


std_data=scaler.transform(input_data_reshaped)
print(std_data)


prediction= classifier.predict(std_data)
print(prediction)


if (prediction[0]==0):
  print('The person is not diabetics')
else:
  print('The person is diabetics')

"""saving the trained model"""

import pickle

filename ='trained_model.sav'
pickle.dump(classifier,open(filename,'wb'))

#loading saved model
loaded_model=pickle.load(open('trained_model.sav','rb'))

input_data=(4,110,92,0,0,37.6,0.191,30)


input_data_as_numpy_array = np.asarray(input_data)


input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)


std_data=scaler.transform(input_data_reshaped)
print(std_data)


prediction= loaded_model.predict(std_data)
print(prediction)


if (prediction[0]==0):
  print('The person is not diabetics')
else:
  print('The person is diabetics')