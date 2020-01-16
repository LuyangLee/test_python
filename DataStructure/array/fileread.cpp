#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    int a[5]{1};
    int *b = new int[5]();
    for(int i=0;i<5;i++)
        cout<<b[i]<<' ';
    return 0;
}