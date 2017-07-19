#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#define G 39.4793

int main()
{
	int n_ts = 10000;
	float dt = 0.001;

	float *datos = malloc((10*8*n_ts)*sizeof(float));
	FILE *file;
	file = fopen("coordinates.csv","r");
	int len = 250;
	char line_buffer[len];
	char *split_buffer;
	const char *delimiter;
	delimiter = ",";
	int i=0;

	while(fgets(line_buffer,len,file)){
		split_buffer = strtok(line_buffer,delimiter);
		while(split_buffer != NULL){
			datos[i] = atof(split_buffer);
			split_buffer = strtok(NULL, delimiter);
			i++;
		}
	}

	for(i=0;i<80;i++){
		printf("%f\n", datos[i]);
	}
	return 0;
}