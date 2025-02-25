#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
#include <deque>
using namespace std;

int N, M;
int infected = 0;
int arr[101][101];
int visited[101];

void init() {
	memset(arr, 0, sizeof(arr));
	memset(visited, 0, sizeof(visited));
	infected = 0;
}

void input() {
	cin >> N;
	cin >> M;
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		arr[a][b] = 1;
		arr[b][a] = 1;
	}
}

void dfs(int depth) {
	// 종료
	/* 
	종료 조건이 애매함 뭔가 막 내가 정해서 끝내면 안된다는 느낌?
	흠.. 어캐 끝내지?
	for 문이 끝까지 알아서 돌다 끝내야함
	*/ 
	visited[depth] = 1;

	//로직
	for (int i = 1; i <= N; i++) {
		//방문 한적 없음 and 연결된 컴퓨터임
		if (arr[depth][i] == 1 && visited[i] == 0) {
			infected += 1;
			dfs(i);
		}
	}
}

int main() {
	init();
	input();
	dfs(1);

	cout << infected;

	return 0;
}