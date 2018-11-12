#include "Stack.h"
#include <iostream>
using namespace std;

template <class T>
Stack<T>::Stack()
{
    m_maxSize = MAX_SIZE;
    m_size = 0;
    m_top = -1;
    m_data = new T[MAX_SIZE];
}

template <class T>
Stack<T>::~Stack()
{
    m_size = 0;
    m_top = -1;
    delete []m_data;
}

template <class T>
void Stack<T>::push(T data)
{
    if (m_top >= MAX_SIZE)
        cout<< "The Stack is Full"<< endl;
        return;
    this->m_top++;
    this->m_data[m_top] = data;
    this->m_size++;
}

template <class T>
T Stack<T>::pop()
{
    if (m_top == -1)
    {
        cout<< "The Stack is empty"<< endl;
        return -1;
    }
    T temp = *(m_data + m_top -1);
    m_top--;
    m_size--;
    return temp;
}

template <class T>
bool Stack<T>::isEmpty()
{
    return (m_top == -1)? true: false;
}


int main()
{
    Stack<int> a;
    a.push(1);
    a.push(1);
    cout<<a.isEmpty()<<endl;
    cout<<a.pop()<<endl;
    return 0;
}