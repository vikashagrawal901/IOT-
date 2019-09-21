import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
x1=np.array([3.393533,3.110073,1.3438029,3.582294,2.280362,7.423437,5.745052,9.172169,7.792783,7.939821])
x2=np.array([2.33127,1.78154,3.36836,4.67918,2.86699,4.69652,3.53399,2.5111,3.42409,0.79164])
y=np.array([1,1,1,1,1,0,0,0,0,0])
x=np.column_stack([x1,x2])
xn1=8.093607

xn2=3.365732

n_d=np.sqrt((x1-xn1)**2+(x2-xn2)**2)
new_nd=[]
print("before sorting")
print(n_d)
print()
print(y)
 
for i in range(len(n_d)):
    for j in range(0,len(n_d)-i-1):
        if n_d[j]>n_d[j+1]:
             n_d[j],n_d[j+1]=n_d[j+1],n_d[j]
             y[j],y[j+1]=y[j+1],y[j]
             
print("after sorting")


    
print(n_d)
print(y)

k=3
y_p=[]
for i in range(0,k):
    y_p.append(y[i])
nn = st.mode(y_p)
print(nn)
