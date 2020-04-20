import numpy as np
import matplotlib.pyplot as plt
n=int(input('Enter the number of steps: '))
h=1/(n-1)
x=np.linspace(0, 1, n)
w=np.zeros(n, dtype=float)
y_true=np.zeros(n, dtype=float)
for i in range(0, n):
    y_true[i]=np.exp(1-9*x[i])
w[0]=2.71828
for i in range(0,n-1):
    w[i+1]=w[i]/(1+9*h)
#print(w)
plt.plot(x,w,color='blue', label='Euler-Backward')
plt.plot(x,y_true, color='green', label='True solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

