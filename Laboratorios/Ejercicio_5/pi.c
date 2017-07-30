#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int n_points = 1000;
float x_min =0.0;
float x_max =1.0;
float y_min =0.0;
float y_max =1.0;

float function(float x);
float pi(void);
void write_file(void);

int main(){
	srand48((unsigned)time(NULL));

	write_file();

	return 0;
}

float function(float x){
	return sqrt(1-(x*x));
}

float pi(void){
	float y_prom=0, int_interval,int_val, pi, pi_temp;
	int n_iterations = 20000000, i,j, n_adentro;
	float x_rand, y_rand, delta;
	int reps = 20;
	for(j = 0; j< reps; j++){
		n_adentro = 0;
		for(i=0;i<n_iterations;i++){
			x_rand = drand48()*(x_max-x_min) + x_min;
			y_rand = drand48()*(y_max-y_min) + y_min;
			delta = function(x_rand) - y_rand;
			if(delta>0.0){
				n_adentro ++;
			}
		}
		int_interval = (x_max-x_min) * (y_max-y_min);
		int_val = int_interval * (1.0*n_adentro/n_iterations);
		pi_temp += 4.0*int_val;
	}
	pi = pi_temp/reps;
	return pi;
}


void write_file(void){
	float PI = pi();

	FILE *fp;

	fp=fopen("results.txt", "a");
	if(fp == NULL)
	    exit(-1);

	fprintf(fp,"El valor de la constante pi es: %f\n", PI);
	fclose(fp);
}

