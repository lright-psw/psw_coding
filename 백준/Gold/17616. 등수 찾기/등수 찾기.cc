#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

const int MAX_N = 100001;

int N;
int M, X;
vector<int> arr[MAX_N];
vector<int> rev[MAX_N];
int visited[MAX_N];
int h, l;


void init() {
	memset(visited, 0, sizeof(visited));
}

void input() {
	cin >> N >> M >> X;
	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		arr[a].push_back(b);
		rev[b].push_back(a);
	}
}

int dfs(int depth) {
	//로직
	visited[depth] = 1;
	int result = 0;

	for (int next : arr[depth]) {
		if (!visited[next]) {
			result += 1 + dfs(next);
		}
	}
	return result;
}

int dfs_rev(int depth) {
	//종료
	//로직
	visited[depth] = 1;
	int result = 0;

	for (int next : rev[depth]) {
		if (!visited[next]) {
			result += 1 + dfs_rev(next);
		}
	}
	return result;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	init();
	input();

	h = dfs_rev(X);

	memset(visited, 0, sizeof(visited));
	l = dfs(X);

	h += 1;
	l = N - l;
	cout << h << "\n" << l;

	return 0;
}