import numpy as np
import matplotlib.pyplot as plt
def dydx(y,x):
    return (y/x-(y/x)**2)
h=0.1
n=11
t=np.linspace(1, 2, n)
w=np.zeros(n, dtype=float)
y_true=np.zeros(n, dtype=float)
for i in range(0, n):
    y_true[i]=t[i]/(1+np.log(t[i]))
w[0]=1
for i in range(0,n-1):
    w[i+1]=w[i]+h*dydx(w[i],t[i])
abserr=np.zeros(n, dtype=float)
relerr=np.zeros(n, dtype=float)
print('t\t\ty\t\ty true\t\tabs err\t\trel err\n')
for i in range(0,n):
    abserr[i]=abs(w[i]-y_true[i])
    relerr[i]=abs((w[i]-y_true[i])/w[i])
    print("{:.3f}".format(t[i]),'\t\t',"{:.3f}".format(w[i]),'\t\t',"{:.3f}".format(y_true[i]),'\t\t',"{:.3f}".format(abserr[i]),'\t\t',"{:.3f}".format(relerr[i]),'\n')
plt.plot(t,w,color='blue', label='Euler-Backward')
plt.plot(t,y_true, color='green', label='True solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

