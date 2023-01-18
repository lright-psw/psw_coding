#include <stdio.h>
#include <stdlib.h>

int static compare(const void* first, const void* second) // 오름차순 비교함수
{
	//void포인터를 in포인터로 변환 후 역참조하여 값을 가져옴
	if (*(int*)first > *(int*)second) //첫번째가 두번째보다 크면 1을 반환
		return 1;
	else if (*(int*)first < *(int*)second) //첫번째가 두번째보다 작음면 -1을 반환
		return -1;
	else //두개의 값이 같으면 0을 반환
		return 0;
}

int main()
{
	int num;
	int arr[1000001] = { 0, };
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		scanf("%d", &arr[i]);
	}
	//정렬할 배열, 요소 개수, 요소 크기, 비교 함수
	qsort(arr, num, sizeof(int), compare);

	for (int i = 0; i < num; i++)
	{
		printf("%d\n", arr[i]);
	}
	printf("\n");

	return 0;
}