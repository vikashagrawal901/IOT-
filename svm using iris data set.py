import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from sklearn.svm import SVC

df=pd.read_csv('E:\iris.csv')
x1=df['SLength']
x2=df['SWidth']
y=df['species']

x=np.column_stack([x1,x2])
print(x)
classifier=SVC()
classifier.fit(x,y)
print("intercept is:",classifier.intercept_)
Y_pred=classifier.predict(x)
print(x,Y_pred)
print("Accuracy is the model of",classifier.score(x,y))
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x1, x2, y, color='black')
plt.xlabel("Slength")
plt.ylabel("SWidth")

##plt.scatter(x1,x2)
plt.show()
