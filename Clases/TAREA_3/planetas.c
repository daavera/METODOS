#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793
//Funciones
int ind(int t,int p);
float acele(float m, float yo, float o, float r);
float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o);
void Leap_Frog(float* m,float* x,float* y,float* z,float* vx,float* vy,float* vz, int n_ts, float dt);

int main(void){
	FILE *fi;
	int n, n_ts;
	float dt = 0.001;
	n_ts = 10000;
	float *m = malloc(10*sizeof(float));
	float *x = malloc((10*n_ts)*sizeof(float));
	float *y = malloc((10*n_ts)*sizeof(float));
	float *z = malloc((10*n_ts)*sizeof(float));
	float *vx = malloc((10*n_ts)*sizeof(float));
	float *vy = malloc((10*n_ts)*sizeof(float));
	float *vz = malloc((10*n_ts)*sizeof(float));

	char temp[100];
	char filename[50] = "coordinates_1.csv";


	fi = fopen(filename, "r");
	if(!fi){
		printf("problems opening the file %s", filename);
		exit(1);
	}
	for(n=0; n<10;n++){
		fscanf(fi, "%f, %f, %f, %f, %f , %f ,%f\n", &m[n],&x[n],&y[n],&z[n],&vx[n],&vy[n],&vz[n]);
	}

	Leap_Frog(m,x,y,z,vx,vy,vz,n_ts,dt);
return 0;
}

//Distancia
float r(float x_yo, float x_o,float y_yo, float y_o,float z_yo, float z_o){
	float dist = pow((pow(x_o-x_yo,2.0) + pow(y_o-y_yo,2.0) + pow(z_o-z_yo,2.0)),0.5);
	printf("%f\n\n",dist);
	return dist;
}

//Aceleracion
float acele(float m,float yo, float o, float r){
	float A = G*m*(o-yo)/pow(r,3.0);
	return A;	
}


// Convertir a index plano
int ind(int t, int p){
	int a = t*10 +p; 
	return a;
}


//Metodo Leap-Frog
void Leap_Frog(float* m, float* x,float* y,float* z,float* vx,float* vy,float* vz, int n_ts, float dt){
	int i, k, j, in, in_o, in_new;
	float Ax, Ay, Az;
	float m_o, x_yo, y_yo, z_yo, x_o, y_o, z_o, r_temp;

	for(k=1;k<3; k++){
		for(j=0;j<10;j++){
			in = ind(k-1,j);
			x_yo = x[in];
			y_yo = y[in];
			z_yo = z[in];
			Ax = 0;
			Ay = 0;
			Az = 0;
			for(i=0;i<10;i++){
				if(i==j){
					continue;
				}
				in_o = ind(k-1,i);
				m_o = m[in];
				x_o = x[in];
				y_o = y[in];
				z_o = z[in];

				r_temp = r(x_yo,x_o,y_yo,y_o,z_yo,z_o);
printf("%f\t %f\t%f\t%f\t%f\n",x_o,y_o, y_o, z_yo, z_o);
				Ax += acele(m_o,x_yo,x_o,r_temp);
				Ay += acele(m_o,y_yo,y_o,r_temp);
				Az += acele(m_o,z_yo,z_o,r_temp);
			}
			in_new = ind(k,j);
			if(k==1){
			//Reemplazo las velocidades iniciales con las velocidades intermedias para generar el desfase
			vx[in] = vx[in] + (0.5*Ax*dt); 
			vy[in] = vy[in] + (0.5*Ay*dt);
			vz[in] = vz[in] + (0.5*Az*dt);

			x[in_new] = x_yo + vx[in]*dt;
			y[in_new] = y_yo + vy[in]*dt;
			z[in_new] = z_yo + vz[in]*dt;
			}
			else{
			vx[in_new] = vx[in] + (Ax*dt); 
			vy[in_new] = vy[in] + (Ay*dt);
			vz[in_new] = vz[in] + (Az*dt);
		
			x[in_new] = x_yo + vx[in]*dt;
			y[in_new] = y_yo + vy[in]*dt;
			z[in_new] = z_yo + vz[in]*dt;
			}
		}
	}	
}


