#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define m 500
#define e 2.718281828
int main()
{
	float y[m], ytr[m], err[m], bnd[m], t[m], h=0.2, M,L;
	int i, j, n;
	n=int(2/h+1);
	y[0]=0.5;
	for(i=0;i<n;i++)
	{
		t[i]=i*h;
		ytr[i]=(t[i]+1)*(t[i]+1)-0.5*pow(e,t[i]);
	}
	for(i=0;i<n-1;i++)
	{
		y[i+1]=y[i]+h*(y[i]-t[i]*t[i]+1);
	}
	L=1; 
	M=0.5*exp(2)-2; // Taken as ~ Max(y''(t))
	for(i=0;i<n;i++)
	{
		err[i]=ytr[i]-y[i];
		bnd[i]=(pow(e,(L*t[i]))-1)*(h*M/(2*L)); 
	}
	printf("t\t\ty\t\ttrue y\t\tErr\t\t\tErr bnd\n");
	for(i=0;i<n;i++)
	{
		printf("%.3f\t\t%.3f\t\t%.3f\t\t%f\t\t%f\n",t[i],y[i],ytr[i],err[i],bnd[i]);
	}
	return 0;
}
