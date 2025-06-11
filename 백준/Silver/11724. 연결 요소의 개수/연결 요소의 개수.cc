#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <sstream>
#include <string>
using namespace std;

const int MAX = 1001;

vector<int> graph[MAX];
bool visited[MAX];

void dfs(int v) {
	visited[v] = true;
	for (auto next : graph[v]) {
		if (!visited[next]) {
			dfs(next);
		}
	}
}

int main() {
	int N, M;
	cin >> N >> M;

	for (size_t i = 0; i < M; i++)
	{
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	int cnt = 0;
	for (size_t i = 1; i <= N; i++)
	{
		if (!visited[i]) {
			dfs(i);
			cnt++;
		}
	}

	cout << cnt << "\n";
	return 0;
}
