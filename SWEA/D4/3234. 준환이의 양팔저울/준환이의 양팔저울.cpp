#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
using namespace std;

int T = 0;
int n = 0;
int rst = 0;
int sum = 0;
int weight[9];
int visited[9] = { 0, };

int factorial(int number) {
	int calc = 1;
	for (int i = 1; i <= number; i++)
	{
		calc *= i;
	}
	return calc;
}

void dfs(int depth, int left, int right) {

	// 종료 조건
	if (depth == n) {
		rst += 1;
		return;
	}

	//가지치기
	if (sum-left <= left) {
		rst += pow(2, n - depth)*factorial(n - depth);
		return;
	}

	// 로직
	// 가지 생성
	// 가지는 왼쪽 오른쪽 2개밖에 없다 
	// 처음 가지를 탐색할 때 무조건 왼쪽부터 한다
	for (int i = 0; i < n; i++) {
		if (!visited[i]) {
			visited[i] = 1;
			dfs(depth + 1, left + weight[i], right);
			if (right + weight[i] <= left)
				dfs(depth + 1, left, right + weight[i]);
			visited[i] = 0;
		}
	}
}

int main() {
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		rst = 0;
		sum = 0;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> weight[i];
			sum += weight[i];
		}
		dfs(0, 0, 0);

		cout << "#" << test_case << " " << rst << "\n";
	}
	return 0;
}