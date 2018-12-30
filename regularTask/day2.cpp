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

int main()
{
    Point a(1,5);
    Point b(2,5);
    cout << a + b;
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
