#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;


int main()
{
    vector <int> a(10);
    // for(int i =0; i < 1000; i ++)
    // {
    //     a.resize(i);
    //     if(!(a.size() == a.capacity()))
    //     {
    //         cout << "# " << i
    //             << "size " << a.size() 
    //             << "  capacity " << a.capacity() << endl;
    //     }
            
    // }
    // cout << a.size() << endl;
    // cout << *(a.end() - 1) << endl;
    // a.erase(a.begin(), a.begin() + 3);
    // cout << a.size() << endl;
    // for(unsigned int i =0; i < a.size(); i ++)
    //     cout << a[i] << '\t';
    // cout << *(a.end() - 1) << endl;


    // cout << *a.begin() <<endl;
    // cout << a.capacity() <<endl;
    // cout << typeid(a.begin()).name() << endl;
    // string s("ming");
    // cout << s.size() <<endl;
    // cout << s.capacity() << endl;
    return 0;
}