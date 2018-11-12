#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 0
// 第40页，二维数组的查找
int find(int *matrix, int m_rows, int m_columns, int number)
{
    int found = false;
    if (matrix != NULL && m_rows > 0 && m_columns > 0)
    {
        int row = 0;
        int column = m_columns - 1;
        while (row < m_rows && column >= 0)
        {
            if (matrix[row * m_columns + column] == number)
            {
                found = true;
                break;
            }
            else if (matrix[row * m_columns + column] > number)
                column--;
            else   
                row++;
        }
    }
    return found;
}

// 第47页，替换空格
void replaceSpace(char str[], int maxLen)
{
    if (str == NULL || maxLen <= 0)
    {
        return;
    }
    int beforeLen = 0;
    int spaceNum = 0;
    int afterLen = 0;
    int i = 0;
    while (str[i] != '\0')
    {
        if (str[i] == ' ')
            ++spaceNum;
        ++beforeLen;
        ++i;
    }
    afterLen = beforeLen + 2*spaceNum;
    if (afterLen > maxLen)
    {
        return;
    }
    int befWord = beforeLen - 1;
    int aftWord = afterLen - 1;
    while (befWord >= 0)
    {
        if(str[befWord] == ' ')
        {
            str[aftWord--] = '0';
            str[aftWord--] = '2';
            str[aftWord--] = '%';
        }
        else
        {
            str[aftWord--] = str[befWord];
        }
        --befWord;
    }
}


int main()
{
    /* 以下测试二维数组查找问题
    int m[4][4] = {
        {1, 2, 8, 9},
        {2, 4, 9, 12},
        {4, 7, 10, 13},
        {6, 8, 11, 15}
    };
    find(*m, 4, 4, 9);
    printf("%d", find(*m, 4, 4, 9));
    */
    // char a[30] = "we are very happy.";
    // replaceSpace(a, 30);
    // printf("%s", a);
    // return 0;

}