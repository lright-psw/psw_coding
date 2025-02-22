#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

#define MAX_WAY 100001

struct Edge {
    int to, length;
};

int N;
int alpha_robot, beta_robot;
int result = 0;
vector<Edge> v[MAX_WAY];
bool visited[MAX_WAY];

int distA[MAX_WAY];
int distB[MAX_WAY];
int current;

void init() {
    for (int i = 0; i <= N; i++) {
        v[i].clear();
    }
    memset(visited, 0, sizeof(visited));
}

void input() {
    cin >> N >> alpha_robot >> beta_robot;
    for (int i = 0; i < N - 1; i++)
    {
        int from, to, length;
        cin >> from >> to >> length;
        v[from].push_back({ to, length });
        v[to].push_back({ from, length });
    }
}

void dfs(int depth, int cost) {
    visited[depth] = 1;

    if (current == 0)
        distA[depth] = cost;
    else
        distB[depth] = cost;

    for (int i = 0; i < v[depth].size(); i++)
    {
        int next = v[depth][i].to;
        int next_cost = v[depth][i].length;
        if (!visited[next]) {
            dfs(next, cost + next_cost);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    init();
    input();

    
    if (alpha_robot == beta_robot) {
        cout << 0;
        return 0;
    }

    memset(visited, 0, sizeof(visited));
    current = 0;
    dfs(alpha_robot, 0);

    memset(visited, 0, sizeof(visited));
    current = 1;
    dfs(beta_robot, 0);

    result = 1e9;
    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < v[i].size(); j++) {
            int tmp = 0;
            int next = v[i][j].to;
            int a = distA[i] + distB[next];
            int b = distA[next] + distB[i];
            if (a < b)
                tmp = a;
            else
                tmp = b;
            if (tmp < result)
                result = tmp;
        }
    }

    cout << result;

    return 0;
}
