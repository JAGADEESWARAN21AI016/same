#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *arr;
    int n,i;
    scanf("%d",&n);
    arr=(int*)malloc(sizeof(int));
    for(i=0;i<n;i++)
    {
        scanf("%d",arr+i);
    }
    printf("Reordered queue: \n");
    int a=n%2==0?n:n-1;
    for(i=0;i<a;i+=2)
    {
        if(*(arr+i+1)<*(arr+i)) 
        {
            printf("%d %d ",*(arr+i+1),*(arr+i));
        }
        else
        {
            printf("%d %d",*(arr+i),*(arr+i+1));
        }
        n%2==0?0:printf("%d",*(arr+n-1));
    }
}
