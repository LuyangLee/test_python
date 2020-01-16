#include<stdio.h>
int main()
{
	int i,k;
	char line[80];
	char op;
	k=0;
	i=0;
	scanf("%c",&op);
    getchar();
	while((line[k]=getchar())!='\n')
	k++;
	line[k]='\0';
	for(i=k-1;i>=0;i--){
		if(line[i]==op){
			printf("index =%d",i);
			break;
		}
	}
	if(i==-1)
	printf("Not Found");
	return 0;
}\\


char s[5][80]