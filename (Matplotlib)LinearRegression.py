import pandas as pd
from sklearn import linear_model
import numpy as np
from google.colab import files
uploaded = files.upload() 
import io
df1=pd.read_csv(io.BytesIO(uploaded['per_capita_income - Sheet1.csv']))
df1
import matplotlib.pyplot as plt
%matplotlib inline
plt.xlabel('year')
plt.ylabel('per capitaincome US')
plt.scatter(df1.year,df1.percapitaincomeUS)
x =df1.drop('percapitaincomeUS',axis='columns')
x
y=df1.percapitaincomeUS
y
reg = linear_model.LinearRegression()
reg.fit(x,y)
reg.predict([[2020]])
reg.coef_
reg.intercept_
