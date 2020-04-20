import numpy as np
import matplotlib.pyplot as plt
#n=int(input('Enter the number of steps: '))
def dydx(y,x):
    return (y/x-(y/x)**2)
h=0.1
n=11
t=np.linspace(1, 2, n)
w=np.zeros(n, dtype=float)
y_true=np.zeros(n, dtype=float)
for i in range(0, n):
    y_true[i]=t[i]/(1+np.log(t[i]))
    #print('In loop y_true \n loop no: ',i+1,'\t t[i]=',t[i],'\t np.log=',np.log(t[i]))
w[0]=1
for i in range(0,n-1):
    w[i+1]=w[i]+h*dydx(w[i],t[i])
#print(t)
#print(y_true)
#print(w)
plt.plot(t,w,color='blue', label='Euler-Backward')
plt.plot(t,y_true, color='green', label='True solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

