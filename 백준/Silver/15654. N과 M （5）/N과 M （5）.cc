#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
#include <queue>
using namespace std;

#define MAX 8

int N, M;
vector<int> arr;
vector<int> number;
vector<bool> visited;

void dfs(int st, int depth) {
	if (depth == M) {
		for (size_t i = 0; i < M; i++)
		{
			cout << arr[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (size_t i = 0; i < N; i++)
	{
		if (!visited[i]) {
			visited[i] = true;
			arr.push_back(number[i]);
			dfs(st + 1, depth + 1);
			arr.pop_back();
			visited[i] = false;
		}
	}

}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	cin >> N >> M;
	visited.resize(N, false);

	for (int i = 0; i < N; i++)
	{
		int tmp;
		cin >> tmp;
		number.push_back(tmp);
	}
	sort(number.begin(), number.end());
	dfs(0, 0);

	return 0;
}