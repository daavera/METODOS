#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int n_points = 1000;
float x_min = 0;
float x_max = 1;

float function(float x);
float integral(void);
void write_file(void);

int main()
{
	float x[n_points];
	srand48((unsigned)time(NULL));

	write_file();

	return 0;
}

float function(float x){
	return exp(-x);
}

float integral(void){
	float y_prom=0, int_val;
	int n_iterations = 2000000, i;
	float rand;

	for (i = 0; i < n_iterations; i++)
	{
		rand = drand48()*(x_max-x_min) + x_min;
		y_prom += function(rand);
	}

	int_val = (x_max-x_min) * y_prom/n_iterations;
	return int_val;
}

void write_file(void){
	float int_val = integral();

	FILE *fp;

	fp=fopen("results.txt", "a");
	if(fp == NULL)
	    exit(-1);

	fprintf(fp,"El valor de la integral es: %f\n", int_val);
	fclose(fp);
}
