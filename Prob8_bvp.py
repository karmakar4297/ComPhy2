import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


#############Fisrt Equation
def first(t,y):
    return np.vstack((y[1],-np.exp(-2*y[0])))
def bc1(ya,yb):
    return np.array([ya[0],yb[0]-np.log(2)])
    
x=np.linspace(1,2,10)
n=x.size
y1=np.zeros((2,n),dtype=float)
y1[0]=0 
sol1=solve_bvp(first,bc1,x,y1)


ytr1=np.zeros(n, dtype=float)
for i in range(0,n):
    ytr1[i]=np.log(x[i])


plt.figure()
plt.plot(x,sol1.sol(x)[0],color='blue',label='First, Numerical')
plt.plot(x,ytr1,'r--',label='First, Analytical')
plt.title(r'$y=log(x)$')
plt.legend()
plt.show()


############Second Equation
def second(t,y):
    return np.vstack((y[1], y[1]*np.cos(t)-y[0]*np.log(y[0]) ))
def bc2(ya,yb):
    return np.array([ya[0]-1, yb[0]-np.exp(1)])
    
x=np.linspace(0,(np.pi)/2)
n=x.size
y2=np.zeros((2,n),dtype=float)
y2[0]=1
sol2=solve_bvp(second,bc2,x,y2)


ytr2=np.zeros(n, dtype=float)
for i in range(0,n):
    ytr2[i]=np.exp(np.sin(x[i]))


plt.figure()
plt.plot(x,sol2.sol(x)[0],color='blue',label='Second, Numerical')
plt.plot(x,ytr2,'r--',label='Second, Analytical')
plt.title(r'$y=exp(sin(x))$')
plt.legend()
plt.show()



########Third Equation
def third(t,y):
    return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(t)**(-1) ))
def bc3(ya,yb):
    return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])
    
x=np.linspace(np.pi/4,np.pi/3)
n=x.size
y3=np.zeros((2,n),dtype=float)
y3[0]=2**(-1/4)
sol3=solve_bvp(third,bc3,x,y2)


ytr3=np.zeros(n, dtype=float)
for i in range(0,n):
    ytr3[i]=np.sqrt(np.sin(x[i]))


plt.figure()
plt.plot(x,sol3.sol(x)[0],color='blue',label='Third, Numerical')
plt.plot(x,ytr3,'r--',label='Third, Analytical')
plt.title(r'$y=\sqrt{sin(x)}$')
plt.legend()
plt.show()



################## Fourth Equation

def fourth(t,y):
    return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(t))))
def bc4(ya,yb):
    return np.array([ya[0]-2, yb[0]-2 ])
    
x=np.linspace(0,np.pi)
n=x.size
y4=np.zeros((2,n),dtype=float)
y4[0]=2
sol4=solve_bvp(fourth,bc4,x,y4)


ytr4=np.zeros(n, dtype=float)
for i in range(0,n):
    ytr4[i]=np.sin(x[i])+2


plt.figure()
plt.plot(x,sol4.sol(x)[0],color='blue',label='Fourth, Numerical')
plt.plot(x,ytr4,'r--',label='Fourth, Analytical')
plt.title(r'$y=\sin{x}+2$')
plt.legend()
plt.show()
