#include<stdio.h>
#include<math.h>


int myfunction(int n) {
    return (n - 1) % 9 + 1;
}

int main()
{
    printf("%d",myfunction(1239));
    return 0;
}
