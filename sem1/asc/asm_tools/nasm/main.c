#include <stdio.h>

int maximum(int, int);

int main()
{
	int a,maxi=-999999;
	scanf("%d", &a);
	maxi = a;
	while (a != 0)
	{
		scanf("%d", &a);
		maxi = maximum(maxi, a);
	}
	printf("The maximum number is %d\n", maxi);
	return 0;
}