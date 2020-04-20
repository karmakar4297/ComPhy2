import numpy as np
import matplotlib.pyplot as plt
def f(r,t):
    x=r[0]
    y=r[1]
    fx=y
    fy=10
    return np.array([fx, fy])
def bound(t,v):
    r=np.array([0,v])
    n=t.size
    x=np.array([0.0])
    for i in range(0,n-1):
        k1 = h*f(r,t[i])
        k2 = h*f(r+k1/2.0,t[i]+h/2.0)
        k3 = h*f(r+k2/2.0,t[i]+h/2.0)
        k4 = h*f(r+k3,t[i]+h)
        r=r+(k1+2*k2+2*k3+k4)/6
        x=np.append(x,r[0])
    return x


h=float(input('Enter step size: '))
n=int(10/h+1)
v1=-100.0
v2=100.0
v=(v1+v2)/2
target=0.01
t=np.linspace(0,10,n)
 # r array with the intitial values for u1, u2 and u3   
#x=np.array([0])
#y=np.array([v])
sol=bound(t,v1)
b1=sol[n-1]
sol=bound(t,v2)
b2=sol[n-1]
while(abs(b2-b1)>target):
    v=(v1+v2)/2
    sol=bound(t,v)
    b=sol[n-1]
    if(b1*b>0):
        v1=v
        b1=b
    else:
        v2=v
        b2=b
    plt.plot(t,sol,'y')
plt.plot(t,sol,'y',label='Candidate')
v=(v1+v2)/2
sol=bound(t,v) #Final Numerical solution
plt.plot(t,sol,'red',label='Final')
y_true=np.zeros(n, dtype=float)
for i in range(0,n-1):
    y_true[i]=5*t[i]*t[i]-50*t[i]
plt.plot(t,y_true,'g--',label='Analytical')    
plt.legend()
plt.show()  
