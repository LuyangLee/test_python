#include<iostream>
#include<algorithm>
using namespace std;
const int maxsize = 100;

int main(int argc, char const *argv[])
{
    int num, q, i, a[maxsize];
    int loop = 0;
    while((cin>>num && cin >> q) == (q && num))
    {
        cout<< "CASE #" << loop++ << endl;
        for(i = 0; i < num; i++)
            scanf("%d",&a[i]);
        sort(a, a + num);
        while(q)
        {
            int x;
            cin >> x;
            int position = lower_bound(a, a + num, x) - a;
            if (a[position] == x)
                cout<< x << "is found in" << position <<endl;
            else
                cout<< x << "is not found"<< endl;
            --q;
        }
    }
    return 0;
}
