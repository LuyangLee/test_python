#include<iostream>
#include<vector>
using namespace std;
void insertSort(int *array, int length)//从小到大排列
{
    int i,j;
    for(i = 1;i < length; i++)
    {
        int temp = array[i];
        for(j = i - 1;j < length && array[j] > temp;j--)
            array[j + 1] = array[j];
        array[j + 1] = temp;
    }
}

int main()
{
    int a[]={-1, -10, 0, 1, 9};
    insertSort(a, 5);
    vector<int> vNum(a, a + 5);
    for(auto item : vNum)
        cout<< item <<endl;
}