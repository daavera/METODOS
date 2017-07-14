#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(void){
	FILE *in;
	int i;
	char nombres[10][100];
	float m[10];
	float x1[10];
	float x2[10];
	float x3[10];
	float v1[10];
	float v2[10];
	float v3[10];

	char temp[100];
	char filename[50] = "coordinates.csv";

	in = fopen(filename, "r");
	if(!in){
		printf("problems opening the file %s", filename);
		exit(1);
	}
	for(i=0; i<10;i++){
		fscanf(in, "%s,%f,%f,%f,%f,%f,%f,%f", temp,&m[i],&x1[i],&x2[i],&x3[i],&v1[i],&v2[i],&v3[i]);
		printf("%d\t%s\t%f\t%f\t%f\t%f\t%f\t%f\t%f", i, temp ,&m[i],&x1[i],&x2[i],&x3[i],&v1[i],&v2[i],&v3[i]);
		//fscanf(in, "%s,%f,%f,%f,%f,%f,%f,%f", temp);
		
		strcpy(nombres[i], temp);

		//printf("%d\t%s\t%f\t%f\t%f\t%f\t%f\t%f\t%f", i, temp ,&m[i],&x1[i],&x2[i],&x3[i],&v1[i],&v2[i],&v3[i]);
	}

return 0;
}
