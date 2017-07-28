#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int N_0=10;
int n_points = 1000;

double linspace(double a, double b, int n, int i);
double function(double t);
void tiempo(double t[]);
void N_t(double t[], double N[]);
void stochastic_walk(double t[], double N[]);
void prom_stochastic(double t[], double N[]);

int main()
{
	srand48((unsigned)time(NULL));

	int i;
	double t[n_points];
	double N[n_points];
	double N_stc[n_points]; 
	double N_prom[n_points]; 

	tiempo(t);
	N_t(t, N);
	stochastic_walk(t,N_stc);
	prom_stochastic(t,N_prom);

	for(i=0; i<n_points; i++){
		printf("%e %e %e %e\n", t[i],N[i],N_stc[i], N_prom[i]);
	}

	return 0;
}

double function(double t){
	double gamma = 0.5;
	return N_0 * exp(-gamma*t);
}

double linspace(double a, double b, int n,int  i){
    double delta =(b-a)/(n-1.0);
    return a +(i*delta);
}

void tiempo(double t[]){
	int i;
	for(i=0;i<n_points;i++){
		t[i] = linspace(0.0,10.0,n_points,i);
	}
}

void N_t(double t[], double N[]){
	int i;
	for(i=0;i<n_points;i++){
		N[i] = function(t[i]);
	}
}


void stochastic_walk(double t[], double N[]){
	N[0] = N_0;
	double gamma = 0.5, dt = fabs(t[1]-t[0]);
	double p, q;
	int i;
	for (int i = 1; i < n_points; ++i){
		if(N[i-1] > 0){
			p = gamma*N[i-1]*dt;
			if(drand48() < p){
				N[i] = N[i-1]-1;
			}
			else{
				N[i] = N[i-1];
			}
		}
		else{
			N[i] = 0;
		}
	}
}

void prom_stochastic(double t[], double N[]){
	int i, j, n_iterations=100;
	double N_temp[n_points];
	for(j=0;j<n_points;j++){
		N[j] = 0;
	}

	for(i = 0; i<n_iterations; i++){
		stochastic_walk(t,N_temp);
		for(j=0;j<n_points;j++){
			N[j] += N_temp[j];
		}
	}

	for(j=0;j<n_points;j++){
		N[j] = N[j]/n_iterations;
	}
}





