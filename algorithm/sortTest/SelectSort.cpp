#include<iostream>
#include<vector>
using namespace std;
 
void selectSort(int *array, int length)// 从小到大排列
{
    for(int i = 0;i < length;i++)
    {
        int key = i;
        for(int j = i + 1;j< length;j++)
        {
            if(array[j] > array[key])
                key = j;
        }
        if(key != i)
        {
            int temp = array[i];
            array[i] = array[key];
            array[key] = temp;
        }
    }
}

int main()
{
    int a[5] = { 9, -1, 0, 10, -9};
    selectSort(a, 5);
    vector<int> vnum(a, a + 5);
    for(auto item :vnum)
    {
        cout <<item <<endl;
    } 
}