import numpy as np
from scipy.integrate import odeint #This is imported to compare only
import matplotlib.pyplot as plt
def NewtonRaphson(yold,t,d):
    flag=0
    ynew=0
    y=yold
    while(flag==0):
        a=(y+20*d*(y-t)**2-2*t*d-yold)
        b=(1+20*d*(y-t))
        ynew=y-a/b
        if (abs((ynew-y)/y)<0.01):
            flag=1
        y=ynew
    return ynew
def model(y,t):
    return -20*np.matmul(np.transpose(y-t),y-t)+2*t
n=int(input('Enter the number of steps: '))
h=1/(n-1)
x=np.linspace(0, 1, n)
w=np.zeros(n, dtype=float)
y_true=np.zeros(n, dtype=float)
#for i in range(0, n-1):
#    y_true[i]=np.exp(1-9*x[i])

w[0]=0.333333
y_true=odeint(model,w[0],x)
for i in range(0,n-1):
    w[i+1]=NewtonRaphson(w[i],x[i+1],h)
#print(w)
plt.plot(x,w,color='blue', label='Euler-Backward')
plt.plot(x,y_true, color='green', label='True solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

