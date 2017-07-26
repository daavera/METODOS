#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

//Dimensiones de los datos
int n_col = 744;
int n_row = 500;


void load_data(int *datos);
int ind(int row, int col);
double random_01(void);
double get_radious(int i_yo, int j_yo, int i_o , int j_o);
int randInRange(int min, int max);
double max_radious(int* datos, int i_yo, int j_yo);

int main(){
	//Definicion de la semilla
	srand((unsigned)time(NULL));

	//Arreglo con los datos
	int *datos = malloc(n_col*n_row*sizeof(int));
	load_data(datos);


	random_01();
	printf("%e\n", random_01());

	return 0;
}

//Conversion a indice lineal
int ind(int row, int col){
	int id 
	if(row >n_row){
		row = row - n_row;
	}
	if(col > n_col){
		col = col - n_col;
	}
	id = n_col*row + col;
	return id;
}

//Generación de número aleatoria 
//(extraida de https://stackoverflow.com/questions/822323/how-to-generate-a-random-number-in-c)
double random_01(void){
    double result;
    result = ((double) rand()/((double) RAND_MAX+1));
    return result;
}

// int randInRange(int min, int max){
// 	int result = min + (int)((double) rand() / (double) (RAND_MAX + 1) * (max - min + 1));
// 	return 
// }

//Calcular el radio
double get_radious(int i_yo, int j_yo, int i_o , int j_o){
    int i;
    double rad, value;
    rad = pow(pow(i_yo - i_o, 2.0) + pow(j_yo - j_o, 2.0), 0.5);
    return rad;
}

double max_radious(int* datos, int i_yo, int j_yo){
	double max=0, r_temp, max_local;
	int i,j,k, cont;
	int adj;
	double *radius_ojo;
	int *radius_check;
	int *ind_ojo;
	k=1;
	while(k<n_row){
		//Radios y distancias que importan
		radius_ojo = malloc((k*2)*sizeof(double));
		adjust_ojo = malloc((k*2)*sizeof(int));
		radius_check = malloc((k*2)*sizeof(int));
		cont = 0;
		for(i=i_yo-k;i<i_yo+k;i++){
			j = j_yo-k;
			radius_ojo[cont] = get_radious(i_yo,j_yo,i,j)
			adj = abs(i-i_yo) + abs(j-j_yo);
			adjust_ojo[cont] = adj;
			cont++;
		}

		//Revisión de los valores en el recuadro con 1
		for(i=i_yo-k;i<=i_yo+k;i++){
			for(j=j_yo-k;j<=j_yo+k;j++){
				if(i==i_yo && j==j_yo){
					continue
				}
				else if(i==i_yo-k || j==j_yo-k || i==i_yo+k || j==j_yo+k){
					adj = abs(i-i_yo) + abs(j-j_yo);
					for(cont=0;cont<=((k*2)-1);cont++){
						if(adjust_ojo[cont] == adj && datos[ind(i,j)]==1){
							radius_check[cont] = -1;
						}
					}
				}
			}
		}

		//Comparación de radios
		for(cont=0;cont<=((k*2)-1);cont++){
			if(radius_check[cont]==-1){
				continue
			}
			else if(radius_ojo[cont] > max){
				max = radius_ojo[cont];
			}
		}

		//Romper los loops
		max_local = 0;
		for(cont=0;cont<=((k*2)-1);cont++){
			if(radius_ojo[cont] > max_local){
				max_local = radius_ojo[cont];
			}
		}
		free(radius_ojo);
		free(adjust_ojo);
		free(radius_check);

		if(max_local>max){
			BREAK A LO ÑAÑA!!!!!!!!!!
		}
	}
	return max;
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
}

