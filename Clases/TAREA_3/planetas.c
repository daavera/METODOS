#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793
int ind(int i,int j);
float acele_x(float m,float x_yo,float x,float r);
float acele_y(float m,float y_yo, float y,float r);
float acele_z(float m,float z_yo, float z, float r);

float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o);
int main(void){
	FILE *in;
	int i;
	float m[10];

	float *x = malloc((10*1000)*sizeof(float));
	float *y = malloc((10*1000)*sizeof(float));
	float *z = malloc((10*1000)*sizeof(float));
	float *vx = malloc((10*1000)*sizeof(float));
	float *vy = malloc((10*1000)*sizeof(float));
	float *vz = malloc((10*1000)*sizeof(float));

	char temp[100];
	char filename[50] = "coordinates_1.csv";


	in = fopen(filename, "r");
	if(!in){
		printf("problems opening the file %s", filename);
		exit(1);
	}
	for(i=0; i<10;i++){
		fscanf(in, "%f, %f, %f, %f, %f , %f ,%f\n", &m[i],&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
	}
 	
	
return 0;
}
float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o){
	float dist = sqrt(pow(x_o-x_yo,2.0)+pow(y_o-y_yo,2.0)+pow(z_o-z_yo,2.0));
	return dist;
}

//Aceleraciones
float acele_x(float m,float x_yo, float x, float r){
	float A = G*m*(x-x_yo)/pow(r,3.0);
	return Ax;	
}
float acele_y(float m,float y_yo, float y, float r){
	float Ay = G*m*(y-y_yo)/pow(r,3.0);
	return Ay;	
}
float acele_z(float m,float z_yo, float z, float r){
	float Az = G*m*(z-z_yo)/pow(r,3.0);
	return Az;	
}

// Convertir a index plano
int ind(int i, int j){
	int a = i*10 +j; 
	return a;
}

		/*
		if((i+1)%8 == 0){
			strcpy(v3[i], temp);
		}
		else if((i+1)%7 == 0){
			strcpy(v2[i], temp);
		}
		else if((i+1)%6 == 0){
			strcpy(v1[i], temp);
		}
		else if((i+1)%5 == 0){
			strcpy(x3[i], temp);
		}
		else if((i+1)%4 == 0){
			strcpy(x2[i], temp);
		}
		else if((i+1)%3 == 0){
			strcpy(x1[i], temp);
		}
		else if((i+1)%2 == 0){
			strcpy(m[i], temp);
		}
		else{
			strcpy(nombres[i], temp);
		}
		*/
