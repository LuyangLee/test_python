#include <iostream>
#include <string>
using namespace std;

class Point
{
    public:
        int Px, Py;
        Point(int x, int y):Px(x), Py(y){}
};

Point operator +(const Point &a, const Point &b)
{
    return Point(a.Px + b.Px, a.Py + b.Py);
}

ostream& operator <<(ostream& out, const Point& a)
{
    out << "(" << a.Px << ","<< a.Py << ")"<<endl;
    return out;
}

istream& operator >>(istream& in, const Point &a)
{
    in >> a.x >>
}

int main()
{
    // int x = 0;
    // while(cin >> x)
    //     cout << x <<endl;
    Point x(1, 2);
    Point y(1, 3);
    cout<< x + y << endl;
    return 0;
}