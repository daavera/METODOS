#include <stdlib.h>
#include <stdio.h>

int main(void)
{
	FILE *in;
	int i;
	int var;
	int test;
	char filename[100] = "new_data.dat";

	printf("Writing to file %s\n", filename);
	
	//WRITE
	in = fopen(filename, "w");
	if(!in){
		printf("problems opening the file %s\n", filename);
		exit(1);
	}
	for (i = 0; i < 10; ++i){
		fprintf(in, "%d\n", i);
	}
	fclose(in);
	
	//APPEND
	in = fopen(filename, "a");
	if(!in){
		printf("problems opening the file %s\n", filename);
		exit(1);
	}
	for (i = 0; i < 10; ++i){
		fprintf(in, "%d\n", i*2 + 10);
	}
	return 0;
	fclose(in);

	//READ
	in = fopen(filename, "r");
	if(!in){
		printf("problems opening the file %s\n", filename);
		exit(1);
	}
	printf("Now I am reading\n");
	for (i = 0; i < 20; ++i){
		fscanf(in,"%d\n", &var);
		printf("value = %d\n", var);
	}
	fclose(in);

	//READ #2
	in = fopen(filename, "r");
	if(!in){
		printf("problems opening the file %s\n", filename);
		exit(1);
	}
	printf("Now I am reading\n");
	do{
		test= fscanf(in, "%d\n", &var);
		if(test != EOF){
			printf("value = %d\n", var);
		}
	}while(test != EOF);
	fclose(in);

	return 0;
}