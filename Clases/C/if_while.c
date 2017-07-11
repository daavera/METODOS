#include <stdio.h>

int main(void)
{
	/* code */
	int a=1;
	int b=2;

	if(a>b){
		printf("a is grater than b: a=%d, b=%d\n", a,b);
	}

	a=1;
	b=1;

	if (a<b){
		printf("a is smaller than b: a=%d, b=%d\n", a,b);
	}

	else{
		printf("a is equal or greater than b: a=%d, b=%d\n", a,b);
	}

	printf("A loop with do-while structure\n");

	a=0;
	b=10;
	do{
		printf("a=%d, b=%d\n", a,b);
		a++;
	}while(a<b);


	return 0;
}