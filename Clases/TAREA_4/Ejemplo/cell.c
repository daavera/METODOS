#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define R0 1.0
#define CHAIN_LENGTH 10000

void MC(char *_name);
double _random(void);
int number_lines(void);
void load_data(double *x, double *y);
double get_radious(double x0, double y0);

int N;
char *name;
double *x_data, *y_data;
double delta = 0.5;

int main(void)
{
    N = 10;

    MC("Canal_ionico");
    MC("Canal_ionico1");

    return 0;
}

void MC(char *_name)
{
    int i;
    double x_new, x_last, y_last, y_new, r_new, r_last, alpha;
    char buffer[100];

    sprintf(buffer, "%s%s", _name, ".txt");
    name = buffer;

    N = number_lines();

    x_data = malloc(N*sizeof(double));
    y_data = malloc(N*sizeof(double));

    load_data(x_data, y_data);

    x_last = 2*_random() - 1;
    y_last = 2*_random() - 1;
    r_last = get_radious(x_last, y_last);

    sprintf(buffer, "%s%s", _name, "_out.dat");
    FILE *file = fopen(buffer, "w");

    for(i=0; i<CHAIN_LENGTH; i++)
    {

        x_new = x_last + (2*_random() - 1)*delta;
        y_new = y_last + (2*_random() - 1)*delta;
        r_new = get_radious(x_new, y_new);
        alpha = exp((r_new - r_last));

        if(alpha > 1)
        {
            alpha = 1;
        }
        if(alpha > _random())
        {
            x_last = x_new;
            y_last = y_new;
            r_last = r_new;
        }
        fprintf(file, "%f %f %f\n", x_last, y_last, r_last);
    }
    fclose(file);
}

double _random(void)
{
    return (double) rand()/RAND_MAX;
}

double get_radious(double x0, double y0)
{
    int i;
    double min, value;
    min = pow(pow(x_data[0] - x0, 2.0) + pow(y_data[0] - y0, 2.0), 0.5) - R0;
    for(i = 1; i<N; i++)
    {
        value = pow(pow(x_data[i] - x0, 2.0) + pow(y_data[i] - y0, 2.0), 0.5) - R0;
        if(value < min)
        {
            min = value;
        }
    }
    return min;
}

int number_lines(void)
{
    int lines = 0, ch;
    FILE *file = fopen(name, "r");
    while(!feof(file))
    {
        ch = fgetc(file);
        if(ch == '\n')
        {
            lines++;
        }
    }
    return lines;
}

void load_data(double *x, double *y)
{
    int i = 0;
    double number;
    FILE *file = fopen(name, "r");

    while(fscanf(file, "%lf", &number)==1)
    {
        if(i%2==0)
        {
            x[i/2] = number;
        }
        else
        {
            y[i/2] = number;
        }
        i += 1;
    }
}