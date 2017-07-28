#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

#define PI 3.1417
//Dimensiones de los datos
int n_col = 744;
int n_row = 500;


void load_data(int *datos);
int ind(int row, int col);
double random_01(void);
double get_radious(int i_yo, int j_yo, int i_o , int j_o);
void write_file(int row_nemo, int col_nemo, double r_nemo);
double max_radious(int* datos, int i_yo, int j_yo);
void MC(int *datos);

int main(){
	int i,j;
	//Definicion de la semilla
	srand48((unsigned)time(NULL));

	//Arreglo con los datos
	int *datos = malloc(n_col*n_row*sizeof(int));
	load_data(datos);

	/*Por alguna razon el primer numero random que genera siempre 
	es muy parecido, por eso me toca llamarlo una vez aqui; lei que 
	aveces asi se inicializa */
	random_01();
	
	MC(datos);
	//printf("%e\n", max_radious(datos,200,740));

	return 0;
}

//Conversion de indices
int ind(int row, int col){
	int id;
	row = row % n_row;
	col = col % n_col;
	if(row < 0){
		row = n_row + row;
	}
	if(col < 0){
		col = n_col + col;
	}
	id = n_col*row + col;
	return id;
}

//Generación de número aleatoria 
//(extraida de https://stackoverflow.com/questions/822323/how-to-generate-a-random-number-in-c)
double random_01(void){
	return drand48();
}

//Calcular el radio
double get_radious(int i_yo, int j_yo, int i_o , int j_o){
    int i;
    double rad, value;
    rad = pow(pow(i_yo - i_o, 2.0) + pow(j_yo - j_o, 2.0), 0.5);
    return rad;
}

//Radio máximo
double max_radious(int* datos, int i_yo, int j_yo){
	float r_max=0;
	double r_temp, r_lim=200;
	int i,j;
	double t,k;
	for (k = 1; k < r_lim; k+=0.5){
		for (t = 0.0; t < 2*PI; t+=0.01){
			i = (k*cos(t))+ i_yo;
			j = (k*sin(t)) + j_yo;
			if(datos[ind(i,j)] == 1){
				goto chao;
			}
		}
		r_max = k;
	}
	chao:
	return r_max;
}

//MC
void MC(int *datos){
	int row_nemo, col_nemo,row_prime, col_prime ;
	double r_nemo, r_prime;
	int dr=200, dc=200;
	int n, n_iterations=10000;
	int agua;
	double alpha, beta;
	float lat,lng;
	agua =1;
	//Iniciales
	while(agua == 1){
		row_nemo = (random_01()*n_row);
		col_nemo = (random_01()*n_col);
		if(datos[ind(row_nemo,col_nemo)] == 0){
			agua=0;
		}
	}
	r_nemo = max_radious(datos,row_nemo,col_nemo); 

	//Markov Chaain
	for(n=0;n<n_iterations;n++){
		agua = 1;
		while(agua == 1){
			row_prime = (2*random_01() - 1)*dr + n_row;
			col_prime = (2*random_01() - 1)*dc + n_col;
			if(datos[ind(row_prime,col_prime)] == 0){
				agua=0;
			}
		}
		r_prime = max_radious(datos,row_prime,col_prime);

		alpha = exp(r_prime - r_nemo);
		if(alpha > 1.0){
			alpha = 1.0;
		}

		beta = random_01();
		if(alpha > beta){
			row_nemo = row_prime;
			col_nemo = col_prime;

			row_nemo = row_nemo % n_row;
			col_nemo = col_nemo % n_col;
			if(row_nemo < 0){
				row_nemo = n_row + row_nemo;
			}
			if(col_nemo < 0){
				col_nemo = n_col + col_nemo;
			}

			r_nemo = r_prime;
		}
	}
	write_file(row_nemo,col_nemo,r_nemo);

	lng = -180.0 + (360.0/n_col)*col_nemo;
	lat = 90.0 - (180.0/n_row)*row_nemo;

	printf("\nLas coordenadas del punto más alejado son: %.3f,%.3f\n\n", lng,lat);
}

//Cargar los datos
void load_data(int *datos){
	FILE *file;
	char filename[50] = "map_data.txt";
	file = fopen(filename,"r");

	int len = 2000;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = " ";
	int i=0, j=0;

	while(fgets(line_buffer,len,file)){
		split_buffer = strtok(line_buffer,delimiter);
		while(split_buffer != NULL){
			datos[ind(i,j)] = atoi(split_buffer);
			split_buffer = strtok(NULL, delimiter);	
			j++;
		}
		j=0;
		i++;
	}

	fclose(file);
}

void write_file(int row_nemo, int col_nemo, double r_nemo){
	FILE *fp;
	char* str = "string";
	int x = 10;

	fp=fopen("results.txt", "w+");
	if(fp == NULL)
	    exit(-1);
	fprintf(fp, "%d %d %e\n", row_nemo, col_nemo, r_nemo);
	fclose(fp);
}
