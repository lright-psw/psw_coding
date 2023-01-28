#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdbool.h>
int main()
{
	char data[11];
	scanf("%s", &data);

	bool flag;
	do
	{
		flag = false;
		for (int i = 1; data[i] > 0; i++)
		{
			if (data[i] > data[i - 1])
			{
				int temp = data[i - 1];
				data[i - 1] = data[i];
				data[i] = temp;
				flag = true;
			}
		}
	} while (flag);

	printf("%s\n", data);

	return 0;
}
