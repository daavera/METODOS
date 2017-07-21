#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.478418

int ind(int t, int p, int dat);
void masas_solares(double* datos);
double r(double* datos, int t, int p1, int p2);
double acele(double* datos, int t , int p1, int p2, int dat);
double acele_total(double* datos, int t , int p, int dat);
void step_inicial(double* datos, double dt);
void Leap_step(double* datos, int t, double dt);

int main()
{
	int n_years = 255;
	int n_py = 1000;
	float dt = 1.0/n_py;
	int n_ts = n_years*n_py;
	//printf("%d\n", n_ts);
	double *datos = malloc(10*8*n_ts*sizeof(double));

	//Leer el archivo
	FILE *file;
	char filename[50] = "coordinates.csv";
	file = fopen(filename,"r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = ",";
	int i=0, j=0, n;

	if(!file){
		printf("problems opening the file %s", filename);
		exit(1);
	}

	while(fgets(line_buffer,len,file)){
		split_buffer = strtok(line_buffer,delimiter);
		while(split_buffer != NULL){
			datos[ind(0,i,j)] = atof(split_buffer);
			split_buffer = strtok(NULL, delimiter);	
			j++;
		}
		j=0;
		i++;
	}

	masas_solares(datos);
	step_inicial(datos, dt);
	for (i = 2; i < n_ts; i++)
	{
		Leap_step(datos, i, dt);
	}

	for(i=0;i<n_ts;i++){
		for(j=0;j<10;j++){
			for(n = 2; n < 5; n++){
				printf("%e", datos[ind(i,j,n)]);
				if(j==9 && n==4)
					continue;
				printf(",");
			}
		}
		printf("\n");
	}

}

//Conversion a indice lineal
int ind(int t, int p, int dat){
	int a = 10*8*t + 8*p + dat; 
	return a;
	}

//Conversion a masa solar
void masas_solares(double* datos){
	int i;
	double masa_solar = 1.9891E30;
	for(i=0;i<10;i++){
		datos[ind(0,i,1)] = datos[ind(0,i,1)]/masa_solar; 
	}
}

//Distancia
double r(double* datos, int t, int p1, int p2){
	double dist=0;
	int i;
	for(i=2;i<5;i++){
		dist += (datos[ind(t,p2,i)]-datos[ind(t,p1,i)])*(datos[ind(t,p2,i)]-datos[ind(t,p1,i)]);
	}
	return pow(sqrt(dist),3.0);
}

//Aceleracion
double acele(double* datos, int t , int p1, int p2, int dat){
	double A;
	A = G*datos[ind(0,p2,1)]*(datos[ind(t,p2,dat)]-datos[ind(t,p1,dat)])/r(datos,t,p1,p2);
	return A;	
}
//Aceleracion total
double acele_total(double* datos, int t , int p, int dat){
	int i;
	double A_T=0;
	for(i=0;i<10;i++){
		if(i == p)
			continue;
		A_T += acele(datos,t,p,i,dat);
	}
	return A_T;
}

void step_inicial(double* datos, double dt){
	int j,k;
	double A;
	for(j=0;j<10;j++){
		for (k = 2; k < 8; ++k){
			if(k==2 || k==3 || k==4){
				datos[ind(1,j,k)] = datos[ind(0,j,k)] + datos[ind(0,j,k+3)]*dt;
			}
			if(k==5 || k==6 || k==7){
				A = acele_total(datos,0,j,k-3);
				datos[ind(1,j,k)] = datos[ind(0,j,k)] + (A*dt);		
			}
		}
	}
}

void Leap_step(double* datos, int t, double dt){
	int j,k;
	double A;
	for(j=0;j<10;j++){
		for (k = 2; k < 8; ++k){
			if(k==2 || k==3 || k==4){
				datos[ind(t,j,k)] = datos[ind(t-2,j,k)] + (2*datos[ind(t-1,j,k+3)]*dt);
			}
			if(k==5 || k==6 || k==7){
				A = acele_total(datos,t-1,j,k-3);
				datos[ind(t,j,k)] = datos[ind(t-2,j,k)] + (A*2*dt);	
			}
		}
	}
}
