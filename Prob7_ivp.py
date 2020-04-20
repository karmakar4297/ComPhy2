import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


#Fisrt Equation
def first(t,y):
    return t*np.exp(3*t)-2*y
sol=solve_ivp(first, [0, 1], [0])
#print(sol.t)
x=np.linspace(0,1,10)
ytr=np.zeros(10, dtype=float)
for i in range(0,10):
    ytr[i]=np.exp(-2*x[i])*(np.exp(5*x[i])*(5*x[i]-1)+1)/25
plt.figure()
plt.plot(sol.t,sol.y[0],color='blue',label='First, Numerical')
plt.plot(x,ytr,color='green',label='First, Analytical')
plt.title(r'$y=e^{-2t}(e^{5t}(5t-1)+1)$')
plt.legend()
plt.show()


#Second Equation
def second(t,y):
    return 1-(t-y)**2
sol=solve_ivp(second, [2, 3], [1])
x=np.linspace(2,2.9,10)
ytr=np.zeros(10, dtype=float)
for i in range(0,10):
    ytr[i]=(x[i]**2-3*x[i]+1)/(x[i]-3)
plt.figure()
#plt.plot(sol.t,sol.y[0],color='blue',label='Second, Numerical')
plt.plot(x,ytr,color='green',label='Second, Analytical')
plt.legend()
plt.title(r'$y=\frac{t^2-3t+1}{t-3}$')
plt.show()
plt.figure()
plt.plot(sol.t,sol.y[0],color='blue',label='Second, Numerical')
plt.legend()
plt.show()


#Third Equation
def third(t,y):
    return 1+y/t
sol=solve_ivp(third, [1, 2], [2])
#print(sol.t)
x=np.linspace(1,2,10)
ytr=np.zeros(10, dtype=float)
for i in range(0,10):
    ytr[i]=x[i]*(np.log(x[i])+2)
plt.figure()
plt.plot(sol.t,sol.y[0],color='blue',label='Third, Numerical')
plt.plot(x,ytr,color='green',label='Third, Analytical')
plt.title(r'$y=t(log(t)+2)$')
plt.legend()
plt.show()

#Fourth Equation
def third(t,y):
    return np.cos(2*t)+np.sin(3*t)
sol=solve_ivp(third, [0, 1], [1])
#print(sol.t)
x=np.linspace(0,1,10)
ytr=np.zeros(10, dtype=float)
for i in range(0,10):
    ytr[i]=(3*np.sin(2*x[i])-2*np.cos(3*x[i])+8)/6
plt.figure()
plt.plot(sol.t,sol.y[0],color='blue',label='Third, Numerical')
plt.plot(x,ytr,color='green',label='Third, Analytical')
plt.title(r'$y=(3sin(2t)-2cos(3t)+8)/6$')
plt.legend()
plt.show()
