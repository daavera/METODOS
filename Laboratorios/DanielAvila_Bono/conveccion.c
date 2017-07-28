#include <stdlib.h>
#include <stdio.h>
#include <math.h>


int n_ts =300, n_xs = 100, c =1;

int ind(int t, int x);
double linspace(double a, double b, int n, int i);
void initial_condition(double *u, double x[n_xs]);
void solver(double *u, double r);

int main()
{
	int i,j;

	double x[n_xs] , t[n_ts];

	//Llenar las listas de x y t
	for(i=0;i<n_xs;i++){
		x[i] = linspace(0.0,2.0,n_xs,i);
	}
	for(i=0;i<n_ts;i++){
		t[i] = linspace(0.0,0.3,n_ts,i);
	}

	double delta_x = fabs(x[1]-x[0]);
	double delta_t = fabs(t[1]-t[0]);
	double r = c * delta_t/delta_x;

	double *u = malloc(n_xs*n_ts*sizeof(double));

	initial_condition(u,x);
	solver(u,r);

	printf("CC,");
	for(i=0;i<n_ts;i++){
		printf("%e", t[i]);
		if(i==(n_ts-1))
			continue;
		printf(",");
	}
	printf("\n");

	for(j=0;j<n_xs;j++){
		printf("%e,", x[j]);
		for(i=0;i<n_ts;i++){
			printf("%e", u[ind(i,j)]);
			if(i==(n_ts-1))
				continue;
			printf(",");
		}
		printf("\n");
	}

	return 0;
}

int ind(int t, int x){
	return n_xs*t + x;
}

double linspace(double a, double b, int n,int  i){
    double delta =(b-a)/(n-1.0);
    return a +(i*delta);
}

void initial_condition(double *u, double x[n_xs]){
	int i, ix;
	for(i=0;i<n_xs;i++){
		ix = ind(0,i);
		if(x[i]>0.7 && x[i]<1.2){
			u[ix] = 1;
		}
		else{
			u[ix] = 0;
		}
	}
}

void solver(double *u, double r){
	int i,j;
	for(i=1;i<n_ts;i++){
		for(j=1;j<(n_xs-1);j++){
			u[ind(i,j)] = u[ind(i-1,j)] - (r*(u[ind(i-1,j)]-u[ind(i-1,j-1)]));
		}
	}
}