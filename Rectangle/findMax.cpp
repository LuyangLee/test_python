#include<iostream>
#include<vector>
#define min(x,y) (x>y?y:x)
#define max(x,y) (x>y?x:y)
using namespace std;

typedef struct info_points
{
    int min_index;
    int max_index;
    float area;
}myPoint;
myPoint p;

myPoint findMax(float a[],int length)
{
    int i = 0;
    int j = length - 1;
    float maxArea = 0;
    while(i < j)
    {
        while(i < j && a[i] <= min_height)
        {
            i++;
            int min_height = min(a[i], a[j]);
            float curArea = min_height * (j - i);
            maxArea = max(maxArea, curArea);
            if (maxArea != curArea)
                p.min_index = i;
        }
            
        while(i < j && a[j] <= min_height)
        {
            j--;
            int min_height = min(a[i], a[j]);
            float curArea = min_height * (j - i);
            maxArea = max(maxArea, curArea);
            if (maxArea != curArea)
                p.max_index = j;
        }
    }
}