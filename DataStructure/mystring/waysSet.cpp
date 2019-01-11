#include<iostream>
#include<string>
using namespace std;

void zsgc()
{
    const char* c1 = "basic1";
    const char* c2 = "reinforce1";
    string s1;
    string s2("0123456");
    string s3(s2, 3, 4);
    cout << "beginning value is "<< s1 << '\t' 
        << s2 << '\t'
        << s3 << endl;
    s1.assign(c1);
    s1.append(c2, 4);
    s1.assign(c1);
    // s1.append(s2, 2, 1);
    // s1.insert(0, c2);
    // s1.replace(0,5, c2);   // make former string from 0 ~ 5 replace with c2(add extral space)
    // s1.append(s2);
    // s1.append(c2);
    // cout << s1.find(s2) << endl;
    // cout << s1.find_first_of(s2) <<endl;
    cout << "--##2-- value is "<< s1 << '\t' 
        << s2 << '\t'
        << s3 << endl;
}

int main()
{
    zsgc();
    return 0;
}