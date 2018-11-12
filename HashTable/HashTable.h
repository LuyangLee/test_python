#include <iostream>
using namespace std;
#define P_NUM 19

template <typename T> class HashTable
{
    private:
        int maxsize;
        int count;
        T *elements;
    public:
        HashTable(int size)
        {
            this->maxsize = size;
            count = 0;
            elements = new T[size];
            if(elements == NULL)
                exit(1);
            else
                for(int i = 0; i < size; i++)
                    elements[i] = 0;
        }
        ~HashTable()
        {
            delete []elements;
        }
        int hash(T value, int p);
        int search(T value);
        void insertHash(T value);
};