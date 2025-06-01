#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

const int MAX = 1001;  

vector<int> graph[MAX];
bool visited_dfs[MAX];
bool visited_bfs[MAX];

void dfs(int v) {
    visited_dfs[v] = true;
    cout << v << " ";
    for (auto next : graph[v]) {
        if (!visited_dfs[next])
            dfs(next);
    } 
}

void bfs(int st) {
    deque<int> dq;
    dq.push_back(st);
    visited_bfs[st] = true;

    while (!dq.empty()) {
        int now = dq.front();
        dq.pop_front();
        cout << now << " ";

        for (auto next : graph[now]) {
            if (!visited_bfs[next]) {
                visited_bfs[next] = true;
                dq.push_back(next);
            }
        }

    }
}

int main() {
    int n, m, v;
    cin >> n >> m >> v;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(v);
    cout << '\n';
    bfs(v);
    cout << '\n';

    return 0;
}
