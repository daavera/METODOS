#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.478418

int ind(int t,int p);
void masas_solares(double* datos);
double acele(double m,double yo, double o, double r);
double r(double x_yo, double x_o,double y_yo, double y_o,double z_yo, double z_o);
void step_1(double* m, double* x,double* y,double* z,double* vx,double* vy,double* vz, double dt);
void Leap_restante(double* m, double* x,double* y,double* z,double* vx,double* vy,double* vz, int n_ts, double dt);

int main()
{
	int n_years = 250;
	int n_py = 30;
	float dt = 1.0/n_py;
	int n_ts = n_years*n_py;
	//printf("%d\n", n_ts);
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
				m[ind(0,i)] = atof(split_buffer);
			else if(j==2)
				x[ind(0,i)] = atof(split_buffer);

			else if(j==3)
				y[ind(0,i)] = atof(split_buffer);

			else if(j==4)
				z[ind(0,i)] = atof(split_buffer);

			else if(j==5)
				vx[ind(0,i)] = atof(split_buffer);

			else if(j==6)
				vy[ind(0,i)] = atof(split_buffer);

			else if(j==7)
				vz[ind(0,i)] = atof(split_buffer);

			split_buffer = strtok(NULL, delimiter);	
			j++;
		}
		j=0;
		i++;
	}

	masas_solares(m);
	//printf("%e\n", m[0]);

	step_1(m,x,y,z,vx,vy,vz,dt);
	//printf("%e\t%e\n", x[ind(0,1)],x[ind(1,1)]);

	Leap_restante(m,x,y,z,vx,vy,vz,n_ts,dt);
	printf("index,X,Y,Z,X2,Y2,Z2\n");
	for (int t = 0; t < n_ts; t++)
	{
		printf("%d,%e,%e,%e,%e,%e,%e\n", t,x[ind(t,0)], y[ind(t,0)],z[ind(t,0)],x[ind(t,4)], y[ind(t,4)],z[ind(t,4)]);
	}

	return 0;
}

//Conversion a indice lineal
int ind(int t, int p){
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
	double A = G*m*(o-yo)/((r*r*r)+0.01);
	return A;	
}

//Leap-inicial
void step_1(double* m, double* x,double* y,double* z,double* vx,double* vy,double* vz, double dt){
	int i, j, in, in_o, in_new;
	double Ax,Ay,Az;
	double r_temp;
	for(j=0;j<10;j++){
		in = ind(0,j);
		Ax = 0;
		Ay = 0;
		Az = 0;
		for(i=0;i<10;i++){
			if(i==j){
				continue;
			}
			in_o = ind(0,i);
			r_temp = r(x[in],x[in_o],y[in],y[in_o],z[in],z[in_o]);
			Ax = Ax + acele(m[in_o],x[in],x[in_o],r_temp);
			Ay = Ay + acele(m[in_o],y[in],y[in_o],r_temp);
			Az = Az + acele(m[in_o],z[in],z[in_o],r_temp);
			}
		in_new = ind(1,j);
		vx[in_new] = vx[in] + (Ax*dt); 
		vy[in_new] = vy[in] + (Ay*dt);
		vz[in_new] = vz[in] + (Az*dt);
		x[in_new] = x[in] + vx[in]*dt;
		y[in_new] = y[in] + vy[in]*dt;
		z[in_new] = z[in] + vz[in]*dt;
	}
}

void Leap_restante(double* m, double* x,double* y,double* z,double* vx,double* vy,double* vz, int n_ts, double dt){
	int i, k, j, in, in_o, in_new, in_2old;
	double Ax,Ay,Az;
	double r_temp;

	for(k=2;k<n_ts; k++){
		for(j=0;j<10;j++){
			in = ind(k-1,j);
			Ax = 0;
			Ay = 0;
			Az = 0;
			for(i=0;i<10;i++){
				if(i==j){
					continue;
				}
				in_o = ind(k-1,i);
				r_temp = r(x[in],x[in_o],y[in],y[in_o],z[in],z[in_o]);
				Ax = Ax + acele(m[in_o],x[in],x[in_o],r_temp);
				Ay = Ay + acele(m[in_o],y[in],y[in_o],r_temp);
				Az = Az + acele(m[in_o],z[in],z[in_o],r_temp);
			}
			in_new = ind(k,j);
			in_2old = ind(k-2,j);
			vx[in_new] = vx[in_2old] + (Ax*dt*2); 
			vy[in_new] = vy[in_2old] + (Ay*dt*2);
			vz[in_new] = vz[in_2old] + (Az*dt*2);

			x[in_new] = x[in_2old] + (2*vx[in]*dt);
			y[in_new] = y[in_2old] + (2*vy[in]*dt);
			z[in_new] = z[in_2old] + (2*vz[in]*dt);
		}
	}
}
