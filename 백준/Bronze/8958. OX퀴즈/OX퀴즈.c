#define CRT_SECURE_NO_WARNING
#include <stdio.h>
#include <string.h>
int main()
{
	int num;
	char ox[80];
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		int count = 1, sum = 0;
		scanf("%s", &ox);
		
		for (int j = 0; j < strlen(ox); j++)
		{
			if (ox[j] == 'O')
			{
				sum += count;
				count++;
			}
			else if (ox[j] == 'X')
			{
				count = 1;
			}
		}
		printf("%d\n", sum);

	}

	return 0;
}