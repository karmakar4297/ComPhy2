#Prob 3: Runge Kutta
import numpy as np
import matplotlib.pyplot as plt
def fxyz(x, y, z):
    return x*np.exp(x)-x+y+2*z
h=float(input('Enter step size: '))
n=int((1/h)+1)
w=np.zeros(n, dtype=float) # rep. y
g=np.zeros(n, dtype=float) #g is dy/dx
w[0]=0
g[0]=0
t=np.linspace(0,1,n)
for i in range(0,n-1):
    k1y=h*g[i]
    k1z=h*fxyz(t[i],w[i],g[i])
    k2y=g[i]+k1z/2
    k2z=fxyz(t[i]+h/2,w[i]+k1y/2,g[i]+k1z/2)
    g[i+1]=g[i]+h*k2z
    w[i+1]=w[i]+h*k2y
plt.plot(t,w,color='blue', label='RK')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$\frac{d^2y}{dx^2}+2\frac{dy}{dx}+y = xe^x-x$')
plt.legend()
plt.show()
    

