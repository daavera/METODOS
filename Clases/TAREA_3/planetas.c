#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793
//Funciones
int ind(int t,int p);
double acele(double m, double yo, double o, double r);
double r(double* x_yo, double* x_o,double* y_yo, double* y_o,double* z_yo, double* z_o);
void Leap_Frog(double* m,double* x,double* y,double* z,double* vx,double* vy,double* vz, int n_ts, double dt);
void masas_solares(double *m);

int main(void){
	FILE *fi;
	int n, n_ts;
	double dt = 0.001;
	n_ts = 10000;
	double *m = malloc(10*sizeof(double));
	double *x = malloc((10*n_ts)*sizeof(double));
	double *y = malloc((10*n_ts)*sizeof(double));
	double *z = malloc((10*n_ts)*sizeof(double));
	double *vx = malloc((10*n_ts)*sizeof(double));
	double *vy = malloc((10*n_ts)*sizeof(double));
	double *vz = malloc((10*n_ts)*sizeof(double));

	char temp[100];
	char filename[50] = "coordinates_1.csv";

	fi = fopen(filename, "r");
	if(!fi){
		printf("problems opening the file %s", filename);
		exit(1);
	}
	for(n=0; n<10;n++){
		fscanf(fi, "%lf, %lf, %lf, %lf, %lf , %lf ,%lf\n", &m[n],&x[n],&y[n],&z[n],&vx[n],&vy[n],&vz[n]);
	}
	masas_solares(m);
	Leap_Frog(m,x,y,z,vx,vy,vz,n_ts,dt);

return 0;
}

//Conversion a masa solar
void masas_solares(double *m){
	int i;
	double masa_solar = 1.9891E30;
	for(i=0;i<10;i++){
		m[i] = m[i]*10*10/masa_solar;
	}
}

//Distancia
double r(double* x_yo, double* x_o,double* y_yo, double* y_o,double* z_yo, double* z_o){
	double dist;
	dist = sqrt((x_o-x_yo)*(x_o-x_yo) + (y_o-y_yo)*(y_o-y_yo) + (z_o-z_yo)*(z_o-z_yo));
	//printf("%lf\n\n",dist);
	return dist;
}

//Aceleracion
double acele(double m,double yo, double o, double r){
	//printf("%2.1f\t %2.1f\t%2.1f\t%2.1f\t\n\n",m,yo,o,r);
	double A = G*m*(o-yo)/pow(r,3.0);
	return A;	
}

// Convertir a index plano
int ind(int t, int p){
	int a = t*10 +p; 
	return a;
}

//Metodo Leap-Frog
void Leap_Frog(double* m, double* x,double* y,double* z,double* vx,double* vy,double* vz, int n_ts, double dt){
	int i, k, j, in, in_o, in_new;
	double *A = malloc(3*sizeof(double));
	double r_temp;


	for(k=1;k<3; k++){
		for(j=0;j<10;j++){
			in = ind(k-1,j);
			A[0] = 0;
			A[1] = 0;
			A[2] = 0;
			for(i=0;i<10;i++){
				if(i==j){
					continue;
				}
				in_o = ind(k-1,i);


				r_temp = r(&x[in],&x[in_o],&y[in],&y[in_o],&z[in],&z[in_o]);
				//printf("%2.1f\t %2.1f\t%2.1f\t%2.1f\n",m[in_o],x[in], x[in_o], r_temp);
				//printf("%lf\t", r_temp);
				A[0] = A[0] + acele(m[in_o],x[in],x[in_o],r_temp);
				A[1] = A[1] + acele(m[in_o],y[in],y[in_o],r_temp);
				A[2] = A[2] + acele(m[in_o],z[in],z[in_o],r_temp);
			}
			in_new = ind(k,j);
			if(k==1){
				//Reemplazo las velocidades iniciales con las velocidades intermedias para generar el desfase
				vx[in] = vx[in] + (0.5*A[0]*dt); 
				vy[in] = vy[in] + (0.5*A[1]*dt);
				vz[in] = vz[in] + (0.5*A[2]*dt);
				x[in_new] = x[in] + vx[in]*dt;
				y[in_new] = y[in] + vy[in]*dt;
				z[in_new] = z[in] + vz[in]*dt;
				printf("POS SEGUNDA: %2.8lf\n", x[in_new]);
			}
			else{
				vx[in_new] = vx[in] + (A[0]*dt); 
				vy[in_new] = vy[in] + (A[1]*dt);
				vz[in_new] = vz[in] + (A[2]*dt);

				x[in_new] = x[in] + vx[in_new]*dt;
				y[in_new] = y[in] + vy[in_new]*dt;
				z[in_new] = z[in] + vz[in_new]*dt;
				printf("NUEVA: %2.8lf\n", x[in_new]);
			}
		}
	}	
}
