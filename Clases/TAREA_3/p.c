#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793

int idx(int t,int p);
void masas_solares(double* datos);
double acele(double m,double yo, double o, double r);
double r(double x_yo, double x_o,double y_yo, double y_o,double z_yo, double z_o);

int main()
{
	int n_ts = 10000;
	float dt = 0.001;

	double *m = malloc(10*sizeof(double));
	double *x = malloc((10*n_ts)*sizeof(double));
	double *y = malloc((10*n_ts)*sizeof(double));
	double *z = malloc((10*n_ts)*sizeof(double));
	double *vx = malloc((10*n_ts)*sizeof(double));
	double *vy = malloc((10*n_ts)*sizeof(double));
	double *vz = malloc((10*n_ts)*sizeof(double));

	//Leer el archivo
	FILE *file;
	char filename[50] = "coordinates.csv";
	file = fopen(filename,"r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = ",";
	int i=0, j=0;

	if(!file){
		printf("problems opening the file %s", filename);
		exit(1);
	}

	while(fgets(line_buffer,len,file)){
		split_buffer = strtok(line_buffer,delimiter);
		while(split_buffer != NULL){

			if(j==1)
				m[idx(0,i)] = atof(split_buffer);
			else if(j==2)
				x[idx(0,i)] = atof(split_buffer);

			else if(j==3)
				y[idx(0,i)] = atof(split_buffer);

			else if(j==4)
				z[idx(0,i)] = atof(split_buffer);

			else if(j==5)
				vx[idx(0,i)] = atof(split_buffer);

			else if(j==6)
				vy[idx(0,i)] = atof(split_buffer);

			else if(j==7)
				vz[idx(0,i)] = atof(split_buffer);

			split_buffer = strtok(NULL, delimiter);	
			j++;
		}
		j=0;
		i++;
	}

	masas_solares(m);
	printf("%e\n", m[0]);
	return 0;
}

//Conversion a indice lineal
int idx(int t, int p){
	int a = 10*t + p; 
	return a;
	}

//Conversion a masa solar
void masas_solares(double *m){
	int i;
	double masa_solar = 1.9891E30;
	for(i=0;i<10;i++){
		m[i] = m[i]/masa_solar;
	}
}

//Distancia
double r(double x_yo, double x_o,double y_yo, double y_o,double z_yo, double z_o){
	double dist;
	dist = sqrt((x_o-x_yo)*(x_o-x_yo) + (y_o-y_yo)*(y_o-y_yo) + (z_o-z_yo)*(z_o-z_yo));
	return dist;
}

//Aceleracion
double acele(double m,double yo, double o, double r){
	//printf("%2.1f\t %2.1f\t%2.1f\t%2.1f\t\n\n",m,yo,o,r);
	double A = G*m*(o-yo)/(r*r*r);
	return A;	
}

//Aceleracion total
// double acele_tot(double* datos, int t, int yo, int coord){
// 	int i;
// 	double A = 0;
// 	double r_temp;
// 	for(i=0;i<10;i++){
// 		if (i == yo){
// 			continue;
// 		}
// 		r_temp = r(datos[idx(t,yo,coordinates)],)
// 		A += acele()
// 	}
// }

