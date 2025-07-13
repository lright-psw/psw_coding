#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;

int N, M;
vector<int> arr;

void dfs(int st, int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << " ";
        cout << "\n";
        return;
    }

    for (int i = st; i <= N; i++)
    {
        arr.push_back(i);
        dfs(i, depth + 1);
        arr.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;
    dfs(1, 0);

    return 0;
}
