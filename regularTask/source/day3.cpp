#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
const int maxsize = 100;

/*
    首先给出数组长度和要解决n个问题,
    然后给出数组，最后给出要查找的数字，返回是否找到
    经过n个循环后重新开始循环。
*/
int main(int argc, char const *argv[])
{
    int num, q, i, a[maxsize];
    vector<int> b;
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
            int position2 = upper_bound(a, a + num, x) - a;
            if (a[position] == x)
                cout<< x << "is found in" << position <<endl;
            else
                cout<< x << "is not found"<< endl;
            --q;
        }
    }
    return 0;
}
