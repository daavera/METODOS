#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
float LeapFrog_step(float x1,float x2, float v1, float v2);

const float G = 6.674 * 10E-11;
float m1 = 1.99 * 10E20;
float x1 = 0.0034386459;
float v1 = -0.0008935944;

float m2= 3.3 * 10E23;
float x2 = 0.3615039791;
float v2 = -1.1184620552;

int main(void){
print("x1\tx2\tv1\tv2\ta1\ta2\n");
LeapFrog_step(x1,x2, v1, v2);

return 0;
}

float LeapFrog_step(float x1_old,float x2_old, float v1_old, float v2_old){
	float h = 0.001;
	float X1 = h*v1_old + x1_old;
	float X2 = h*v2_old + x2_old;

	float V1 = h*a1_old + v1_old;
	float V2 = h*a2_old + v2_old;
	
	float A1 = (G*m2)/((x1-x2)*(x1-x2));
	float A2 = (G*m1)/((x2-x1)*(x2-x1));
	
	print("%f\t%f\t%f\t%f\t%f\t%f\n",(X1,X2, V1, V2,A1,A2));	
}


