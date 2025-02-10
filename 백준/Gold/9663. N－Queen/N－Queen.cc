#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include <vector>
#include <cstring>
using namespace std;

int n = 0;
int rst = 0;
int col[15]; // 열

//행을 기준으로 재귀
void dfs(int row) {

	//종료 조건
	if (row == n) {
		rst += 1;
		return;
	}

	//로직
	for (int i = 0; i < n; i++)
	{
		int flag = 1;
		for (int j = 0; j < row; j++)
		{
			if (col[j] == i || abs(col[j] - i) == (row - j)) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			col[row] = i;
			dfs(row + 1);
		}
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	memset(col, 0, sizeof(col));
	cin >> n;
	dfs(0);

	cout << rst;
	return 0;
}