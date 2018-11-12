#include "Student.h"


template <class T>
inline void Student<T>::print()
{
    cout<< age<< endl;
}

template <class T>
Student<T> Student<T>::operator +(const Student<T>& A)
{
	Student<T> s(this.age + A.age ,this.age + A.num); 
    return s;
}


template <class T>
Student<T>::Student(T a, T n):age(a),num(n)
{}

int main()
{
    Student<int> s(2, 1);
    Student<int> y(3, 2);
    s + y;
    s.print();
    return 0;
}