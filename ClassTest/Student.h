#include<iostream>
#include<iomanip>
using namespace std;

template <class T>
class Student
{
    private:
        T age;
        T num;
    public:
        inline void print();
        Student(T a,T n);
        Student<T> operator +(const Student<T>& A);
};