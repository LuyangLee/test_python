#include<iostream>
#include<vector>
using namespace std;

#if 1
void bubblesort(int *array, int length)
{
    for(int i = 0; i < length; i++)
    {
        for(int j = i + 1; j < length; j++)
        {
            if(array[i] > array[j])
            {
                int temp = array[j];
                array[j] = array[i];
                array[i] = temp;
            }
        }
    }
}
#endif

int main()
{
    int a[5] = { 9, -1, 0, 10, -9};
    bubblesort(a, 5);
    vector<int> vnum(a, a + 5);
    for(auto item :vnum)
    {
        cout <<item <<endl;
    } 
}