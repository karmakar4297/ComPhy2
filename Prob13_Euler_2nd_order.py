import numpy as np
import matplotlib.pyplot as plt
def g(u,y,t):
    return (2*t*u-2*y+t**3*np.log(t))/(t**2)
h=0.001
n=int(1/h+1)
t=np.linspace(1,2,n)
y=np.zeros(n, dtype=float)
u=np.zeros(n, dtype=float)
y[0]=1
u[0]=0
for i in range(0,n-1):
    u[i+1]=u[i]+h*g(u[i],y[i],t[i])
    y[i+1]=y[i]+h*u[i]
ytr=np.zeros(n, dtype=float)
for i in range(0,n):
    ytr[i]=7*t[i]/4+(t[i]**3/2)*np.log(t[i])-(3/4)*t[i]**3
plt.plot(t,y,color='blue',label='Euler')
plt.plot(t,ytr,'g--',label='True sol')
plt.legend()
plt.show()
