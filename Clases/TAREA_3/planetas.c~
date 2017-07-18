#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793
//Funciones
int ind(int i,int j);
float acele(float m,float yo,float o,float r);
float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o);

int main(void){
	FILE *in;
	int i, k, j, n_ts;
	float Ax, Ay, Az;
	float dt = 0.001;
	float m[10];
	n_ts = 100000
	float *x = malloc((10*n_ts)*sizeof(float));
	float *y = malloc((10*n_ts)*sizeof(float));
	float *z = malloc((10*n_ts)*sizeof(float));
	float *vx = malloc((10*n_ts)*sizeof(float));
	float *vy = malloc((10*n_ts)*sizeof(float));
	float *vz = malloc((10*n_ts)*sizeof(float));

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
	
	for(k=1;k<1000; k++){
		for(j=0;j<10;j++){
			int in = ind(k-1,j);
			float x_yo = x[in];
			float y_yo = y[in];
			float z_yo = z[in];
			Ax = 0;
			Ay = 0;
			Az = 0;
			for(i=0;i<10;j++){
				if(i==j){
					continue;
				}
				int in_o = ind(k-1,i);
				float m_o = m[i];
				float x_o = x[in];
				float y_o = y[in];
				float z_o = z[in];
				float r_temp = r(x_yo,x_o,y_yo,y_o,z_yo,z_o);
				Ax += acele(m_o,x_yo,x_o,r);
				Ay += acele(m_o,y_yo,y_o,r);
				Az += acele(m_o,z_yo,z_o,r);
			}
			float vx_int = vx[in] + (0.5*Ax*dt); 
			float vy_int = vy[in] + (0.5*Ay*dt);
			float vz_int = vz[in] + (0.5*Az*dt);
			
			int in_new = ind(k,j);
			x[in_new] = x_yo + vx_int*dt;
			y[in_new] = y_yo + vy_int*dt;
			z[in_new] = z_yo + vz_int*dt;	
		}
	}
return 0;
}

//Distancia
float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o){
	float dist = sqrt(pow(x_o-x_yo,2.0)+pow(y_o-y_yo,2.0)+pow(z_o-z_yo,2.0));
	return dist;
}

//Aceleracion
float acele(float m,float yo, float o, float r){
	float A = G*m*(o-yo)/pow(r,3.0);
	return A;	
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
