#10th
import numpy as np
import matplotlib.pyplot as plt
def f(y,u):
    return 1/(y**2*(1-u)**2+u**2)
def rk4(w,u,h,i):
    k1 = h*f(w[i],u[i])
    k2 = h*f(w[i]+k1/2.0,u[i]+h/2.0)
    k3 = h*f(w[i]+k2/2.0,u[i]+h/2.0)
    k4 = h*f(w[i]+k3,u[i]+h)
    return  w[i]+(k1+2*k2+2*k3+k4)/6
h=float(input('Enter step size: '))
n=int((1/h)+1)
#u=np.linspace(0,1,n)
u=np.array([0])
w=np.zeros(1)

t=np.linspace(0,1,n-1)
x=np.zeros(t.size)
x[0]=1
flag=0
w[0]=1
hold=0

for i in range(0,n-2):
    x[i+1]=rk4(x,t,h,i)

i=0
while(flag==0):
    temp=rk4(w,u,h,i)
    if(flag==0):
        #print(u[i]/(1-u[i]))
        if((u[i])>=0.999999714):
            flag=1
            hold=w[i]
    w=np.append(w,temp)
    u=np.append(u,u[i]+h)
    i=i+1
for i in range(0,n-1):
    t[i]=t[i]/(1-t[i])
plt.plot(t,x,color = 'b')
#plt.legend()
plt.show()
print('x at t = 3.5x10^6', 'is approximately: ',hold)
#print(u.size)
#print(x)
