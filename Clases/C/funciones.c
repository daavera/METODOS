#include <stdio.h>
#define PI 3.14159

void print_points(int n_points);
float get_surface(float radius);
float get_volume(float radius);

int main(int argc, char const *argv[])
{
	int n_points=12;

	print_points(n_points);
	return 0;
}

void print_points(int n_points){
	int i;
	float radius = 0.0;
	float volume = 0.0;
	float surface = 0.0;

	printf("Radius Surface Volume\n");
	for(i=0;i<n_points;i++){
		radius=1.0*i;
		surface = get_surface(radius);
		volume = get_volume(radius);

		printf("%f %f %f\n", radius,surface,volume);
	}
}

float get_surface(float radius){
	float sur = 4.0*PI*radius*radius;
	return sur;
}

float get_volume(float radius){
	float vol = (4.0/3)*PI*radius*radius*radius;
	return vol;
}