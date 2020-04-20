import numpy as np
import matplotlib.pyplot as plt
def f(r,t):
    u1=r[0]
    u2=r[1]
    u3=r[2]
    f1=u1+2*u2-2*u3+np.exp(-t)
    f2=u2++u3-2*np.exp(-t)
    f3=u1+2*u2+np.exp(-t)
    return np.array([f1, f2, f3])

h=float(input('Enter step size: '))
n=int(1/h+1)
t=np.linspace(0,1,n)
r=np.array([3,-1,1]) # r array with the intitial values for u1, u2 and u3   
u1=np.array([3])
u2=np.array([-1])
u3=np.array([1])
for i in range(0,n-1):
    k1 = h*f(r,t[i])
    k2 = h*f(r+k1/2.0,t[i]+h/2.0)
    k3 = h*f(r+k2/2.0,t[i]+h/2.0)
    k4 = h*f(r+k3,t[i]+h)
    r=r+(k1+2*k2+2*k3+k4)/6
    u1=np.append(u1,r[0])
    u2=np.append(u2,r[1])
    u3=np.append(u3,r[2])
plt.plot(t,u1,color='blue', label='u1')
plt.plot(t,u2,color='red', label='u2')
plt.plot(t,u3,color='black', label='u3')
plt.legend()
plt.show()
