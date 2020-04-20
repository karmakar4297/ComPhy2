#Prob 6: Solving Diff Eqn using Relaxation Method
#Siddhartha Karmakar

import numpy as np
import matplotlib.pyplot as plt
h=1 #Step size
n=int((10/h)+1)
N=90 #Number of iterations
w=np.zeros((N+1,n), dtype=float)
y_true=np.zeros(n, dtype=float)
t=np.linspace(0,10,n)
w[:,0]=0
w[:,n-1]=0
j=0
m=N
while(N):
    for i in range(1,n-1):
        w[j+1,i]=(w[j,i+1]+w[j,i-1]-10*h**2)/2 #Solving linear eqns by Jaccobi Method
    j=j+1
    N=N-1
for j in range(1,m-2):
    #plt.figure()
    plt.plot(t,w[j],color='blue',) #Candidate
    #print(j)
    #plt.legend()
plt.plot(t,w[j],color='blue', label='Candidate Solution') #Candidate
plt.plot(t,w[m],color='red', label='Numerical Solution') #Final
for i in range(0,n):
    y_true[i]=5*t[i]*t[i]-50*t[i]
    
plt.plot(t,y_true,color='green', label='True Solution') #True sol
plt.legend()
plt.title(r'$\frac{d^2x}{dt^2}-10=0$')
plt.xlabel('t')
plt.ylabel('x')
plt.show()   

