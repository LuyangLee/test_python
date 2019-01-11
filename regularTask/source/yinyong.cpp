#include <iostream>
using namespace std;

void change(int *a)
{
    a = (int *)malloc(sizeof(int));
    *a = 5;
}

void anotherChange(int *&a)
{
    a = (int *)malloc(sizeof(int));
    *a = 5;
}
int main()
{
    int *a, *b;
    change(a);
    anotherChange(b);
    cout<< *a<<endl;
    cout<< *b<<endl;
}