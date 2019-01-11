#include <iostream>
#include <algorithm>
using namespace std;

void myswap(int& a, int& b)
{
    int t = a;
    a = b;
    b = t;
}

int main()
{
    int a, b;
    while(cin >> a >> b)
    {
        myswap(a, b);
        cout << min(a, b) << endl;
        cout << "a " << a << "b "<< b<<endl;
    }
    return 0;
}