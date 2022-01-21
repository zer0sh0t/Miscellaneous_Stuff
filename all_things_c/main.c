#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "utils.h"

void string_tests()
{
    char x[6];
    scanf("%5s", x);
    getchar();
    printf("%s\n", x);
    printf("%d\n", strlen(x));
}

void print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
}

void double_arrv(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        arr[i] *= 2;
    }
}

void pointer_tests()
{
    int x = 42;

    int *p;
    p = &x;
    // int *p = &x;

    printf("%d %p %p %d %d\n", x, &x, p, *p, *&x);
    x++;
    printf("%d %d\n", x, *p);
    (*p)++;
    printf("%d %d\n", x, *p);
    printf("%d %p %p %d %d\n", x, &x, p, *p, *&x);
}

int incr_this(int *x)
{
    (*x)++;
    return *x;
}

// void swap(int x, int y)
// {
//     int temp = x;
//     x = y;
//     y = temp;
// }

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

typedef struct
{
    int x, y;
} Point;

void struct_tests()
{
    Point p = {1, 2};
    printf("%d %d\n", p.x, p.y);
    p.x = 3;
    p.y = 4;
    printf("%d %d\n", p.x, p.y);
    Point ps[] = {{1, 2}, {3, 4}};
    printf("%d %d\n", ps[0].x, ps[0].y);
}

void struct_pointer()
{
    Point p = {1, 2};
    Point *pp = &p;
    printf("%p\n", pp);
    printf("%d %d %d %d\n", p.x, p.y, pp->x, pp->y);
}

void write_files()
{
    FILE *fp = fopen("test.txt", "a"); // w, a
    fprintf(fp, "Hello World!\n");
    fclose(fp);
}

void read_files()
{
    char line[100];
    FILE *fp = fopen("test.txt", "r");
    fgets(line, 100, fp);
    fgets(line, 100, fp);
    fgets(line, 100, fp);
    printf("%s", line);
    fclose(fp);
}

void num_file_lines()
{
    int lcount = 0;
    char curr_char;
    FILE *fp = fopen("test.txt", "r");
    curr_char = getc(fp);
    while (curr_char != EOF)
    {
        if (curr_char == '\n')
        {
            lcount++;
        }
        curr_char = getc(fp);
    }
    fclose(fp);
    printf("%d\n", lcount);
}

void char_pointers()
{
    char a = 'a';
    char *ap = &a;
    printf("%c %c %d %d\n", a, *ap, &a, ap);
}

void dyn_arrs()
{
    int const size = 4;
    int *arr = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
    {
        arr[i] = i + 1;
    }

    for (int i = 0; i < size; i++)
    {
        printf("mem location: %d ", &arr[i]);
        printf("value: %d ", arr[i]);
        printf("\n");
    }
    printf("\n");

    int const new_size = size / 2;
    int *arr1 = (int *)realloc(arr, new_size * sizeof(int));
    free(arr);
    
    for (int i = 0; i < size; i++)
    {
        printf("mem location: %d ", &arr1[i]);
        printf("value: %d ", arr1[i]);
        printf("\n");
    }
    free(arr1);
}

void dyn_chr()
{
    int const size = 6;
    char *p = (char *)malloc(size * sizeof(char));
    p = "Hello";
    printf("%s %d\n", p, strlen(p));
    
    int i = 0;
    while (*(p + i) != '\0')
    {
        printf("%c ", *(p + i));
        i++;
    }
    free(p);
}

void dyn_int()
{
    int a = 10;
    int *p = (int *)malloc(sizeof(int));
    p = &a;
    printf("%d %d %d %d\n", p, &a, &p, *p);
    int **q = (int **)malloc(sizeof(int));
    q = &p;
    printf("%d %d %d %d %d\n", q, &p, &q, *q, **q);
    free(p);
    free(q);
}

int *add(int *a, int *b)
{
    int *c = (int *)malloc(sizeof(int));
    *c = (*a) + (*b);
    printf("%d %d %d\n", c, &c, *c);
    return c;
}

void pt_as_fn()
{
    int a = 2, b = 4;
    // int *c = add(&a, &b);
    // int *p = c;
    int *p = add(&a, &b);
    printf("%d\n", *p);
    free(p);
}

int Add(int a, int b)
{
    return a + b;
}

void fn_pt()
{
    int c;
    int (*p)(int, int);
    p = Add;
    c = p(2, 4);
    printf("%d \n", c);
}

void call_from_utils()
{
    int a = 2;
    int b = 3;
    double c = add_from_utils(a, b);
    printf("%f\n", c);
}

int main()
{
    int x;
    scanf("%i", &x);
    getchar(); // to clear the input buffer
    double y = (double) x / 2;
    printf("%f", y);

    // char name[11];
    // scanf("%s", name);
    // getchar();
    // printf("Hello %s!", name);

    // double num;
    // scanf("%lf", &num);
    // getchar();
    // printf("%lf", num);

    // char x;
    // scanf("%c", &x);
    // printf("%c -> %i\n", x, x);

    // int y;
    // scanf("%i", &y);
    // printf("%i -> %c\n", y);

    // char qwerty = 'A' + '\t';
    // printf("%c(%i)", qwerty, qwerty);

    // _Bool s = 42;
    // printf("%i\n", s);

    // bool s = true;
    // printf("%i\n", s);

    // srand(time(NULL));
    // int num = rand();
    // printf("%d\n", num);

    // char x[] = {'a', 'b', '\0'};
    // printf("%s", x);

    // char y[3];
    // y[0] = 'c';
    // y[1] = 'd';
    // y[2] = '\0';
    // printf("%s", y);

    // int arr[3] = {1, 2, 3};
    // int size = sizeof(arr) / sizeof(int);
    // printf("%d", size);

    // int marr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // int row = sizeof(marr) / sizeof(marr[0]);
    // int col = sizeof(marr[0]) / sizeof(marr[0][0]);
    // int ele = sizeof(marr) / sizeof(marr[0][0]);

    // printf("%d %d %d\n\n", row, col, ele);

    // for (int i = 0; i < row; i++)
    // {
    // 	for (int j = 0; j < col; j++)
    // 	{
    // 		printf("%d ", marr[i][j]);
    // 	}
    // 	printf("\n");
    // }

    // char x[6] = "hello";
    // printf("%d\n", sizeof(x) / sizeof(x[0]));
    // printf("%s\n", x);
    // printf("%d\n", sizeof(char));

    // char x[5];
    // scanf("%s", x);
    // getchar();
    // printf("%s\n", x);
    // printf("%c\n", x);

    // string_tests();

    // int arr[] = {1, 2, 3};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // print_array(arr, size);

    // int x = 12;
    // printf("%p\n", &x);

    // pointer_tests();
    // int a = 2;
    // int b = incr_this(&a);
    // printf("%d\n", b);

    // int a = 2;
    // int b = 3;
    // printf("%d %d\n", a, b);

    // swap(&a, &b); // swap(a, b);
    // printf("%d %d\n", a, b);

    // struct_tests();
    // struct_pointer();
    // write_files();
    // read_files();
    // num_file_lines();
    // char_pointers();
    // dyn_arrs();
    // dyn_chr();
    // dyn_int();

    // int arr[] = {1, 2, 3};
    // int size = sizeof(arr) / sizeof(arr[0]);
    // double_arrv(arr, size);
    // print_array(arr, size);
    // pt_as_fn();
    // fn_pt();
    // call_from_utils();

    return 0;
}
