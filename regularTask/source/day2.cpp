#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Point
{
    public:
        int x, y;
        Point(int px = 0, int py = 0): x(px), y(py) {}
};

Point operator + (const Point &a, const Point &b)
{
    return Point(a.x + b.x, a.y + b.y);
}

ostream& operator <<(ostream &out, const Point &a)
{
    out << "(" << a.x << "," << a.y << ")" <<endl;
    return out;
}

istream& operator >>(istream& in, Point &a)
{
    in >> a.x >> a.y;
    return in;
}

bool operator ==(const Point& a, const Point& b)
{
    return (a.x == b.x) && (a.y == b.y) ? true : false; 
}

int main()
{
    Point a, b;
    while (cin >> a)
    {
        cout << "b will be inputed"<< endl;
        while(cin >> b)
        {
            cout<< a << endl;
            cout << b << endl;
            if (a == b) 
                cout << a + b << endl;
            else   
                break;
        }   
        cout<< "x will be input" << endl;
    }
    /*
    string line;
    while(getline(cin, line))
    {
        int sum , i = 0;
        string x;
        stringstream ss(line);
        while(ss >> x) 
            cout << x << '\t';
    }
    return 0;
    */
}
