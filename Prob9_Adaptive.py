import numpy as np
import matplotlib.pyplot as plt
def f(y,t):
    return (y**2+y)/t
def rk4(w,x,h,i):
    k1 = h*f(w[i],x[i])
    k2 = h*f(w[i]+k1/2.0,x[i]+h/2.0)
    k3 = h*f(w[i]+k2/2.0,x[i]+h/2.0)
    k4 = h*f(w[i]+k3,x[i]+h)
    return  w[i]+(k1+2*k2+2*k3+k4)/6
h=0.1
x=np.zeros(1, dtype=float)
x[0]=1
w1=np.zeros(1, dtype=float)
w2=np.zeros(1, dtype=float)
i=0
delta=0.0001
w1[0]=-2
w2[0]=-2
flag=0
while(x[i]<3):
    temp1=rk4(w1,x,h,i)
    temp2=rk4(w2,x,2*h,i)
    err=abs((temp2-temp1)/30)
    hp=h*(delta*h/err)**(1/4)
    if(err>delta):
        flag=1
        h=hp
        temp1=rk4(w1,x,h,i)
        temp2=rk4(w2,x,2*h,i)
        w1=np.append(w1,temp1)
        w2=w1
    else:
        w1=np.append(w1,temp1)
        w2=w1
    x=np.append(x,x[i]+h)
    #print(x.size, h)
    #print(err)
    i=i+1
#print(w1)
plt.plot(x,w1,color = 'b',label = 'Adaptive')
plt.legend()
plt.show()
    
        
