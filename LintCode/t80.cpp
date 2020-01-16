#include<stdio.h>
int isFuYin(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        if (c=='A' || c=='E' || c=='I' || c=='O' || c=='U')
        {
            return 0;
        }
        else
        {
            return 1;
        }
    }
    else
        return 0;
}
int main()
{
    char c = 'a';
    int count = 0;
    while ((c = getchar()) != '\n')
    {
        if (isFuYin(c))
            count++;
    }
    printf("%d",count);
    return 0;
}