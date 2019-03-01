#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <algorithm>
#define len(a) sizeof(a)/sizeof(a[0])
using namespace std;

/*
    巧妙的读取方法是，每读取一个字符，便处理该字符，加入到set里面
*/
int main()
{
    string s, buf;
    string a, b;
    while (cin >> s )
    {
        cout << s << endl;
        for (unsigned int i = 0; i < s.length(); i ++)
        {
            if (isalpha(s[i]))
                s[i] = tolower(s[i]);
            else
                s[i] = ' ';
        }
        cout << s << endl;
    }
    return 0;
}