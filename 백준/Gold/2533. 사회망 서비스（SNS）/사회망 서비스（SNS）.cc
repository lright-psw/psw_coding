#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

const int MAX_N = 1000000;

int N;
vector<int> tree[MAX_N];
bool visited[MAX_N];
int result = 0;


void init() {
	memset(tree, 0, sizeof(tree));
	memset(visited, false, sizeof(visited));
}

void input() {
	cin >> N;
	result = 0;
	for (int i = 0; i < N-1; i++)
	{
		int a, b;
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a);
	}
}

// 얼리어답터는 누가 친구이던 알 필요가 없음
// 일반인은 반드시 모든 친구가 얼리어답터여야함
// 지금 한 노드가 가질수 있는 형태는 2가지야
// 무조건 어답터가 아니면 일반인임
int dfs(int depth) {
	visited[depth] = true;

	// 노드의 상태는 2종류 일반인 아님 어답터
	int status[2] = { 0,0 };

	// 가지 분할
	for (int i = 0; i < tree[depth].size(); i++)
	{
		int next = tree[depth][i];
		if (visited[next] == false) {
			status[dfs(next)] += 1;
		}
	}

	// 일반인&어답터 판별
	// 만약 주변이 일반인이면
	if (status[0] > 0) {
		result += 1;
		return 1;
	}

	return 0;
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	input();
	dfs(1);

	cout << result;

	return 0;
}