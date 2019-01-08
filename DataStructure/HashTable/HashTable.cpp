#include "HashTable.h"

template<typename T>
int HashTable<T>::hash(T value, int p)
{
    return value % p;
}

template <typename T>
int HashTable<T>::search(T value)
{
    int p = hash(value, P_NUM);
    if(elements[p] == value)
        return p;
    int rp = (p + 1) % this->maxsize;
    while(rp == p)
    {
        if(elements[rp] == value || elements[rp] == 0)
            return rp;
    } 
    if(rp == p)
    {
        return -1;
    }
}

template <typename T>
void HashTable<T>::insertHash(T value)
{
    int pos = hash();
}

int main()
{
    HashTable<int> h = HashTable<int>(20);
    cout<<h.search(15)<<endl;
    return 0;
}

