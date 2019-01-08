#include<iostream>
#include<vector>
using namespace std;

int partition(int *a, int left, int right)
{
    int sign = a[left];
    while(left < right)
    {
        while(left < right && a[right] > sign)
            right--;
        if(left < right)
            a[left++] = a[right];
        while(left < right && a[left] < sign)
            left++;
        if(left < right)
            a[right--] = a[left];
    }
    a[left] = sign;
    return left;
}

void quicksort(int *array, int l, int r)
{
    if(l >= r)
        return;
    else
    {
        int q = partition(array, l, r);
        quicksort(array, l, q - 1);
        quicksort(array, q + 1, r);
    }
}

int main()
{
    int a[] = {-1, 3, 0, 9, 4};
    quicksort(a, 0, 4);
    vector<int> vNum(a, a + 5);
    for (auto item:vNum)
        cout<<item<<endl; 
}