#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

const int MAX_N = 1001;

struct Edge {
    int u, v;
    double weight;
};

int N, M, cnt = 0;
int parent[MAX_N];
pair<int, int> god[MAX_N];
vector<Edge> edges;
double result = 0.0;

// Find
int find(int x) {
    if (x == parent[x]) return x;
    return parent[x] = find(parent[x]);
}

// Union
void union_sets(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        parent[b] = a;
        cnt++;  // MST 간선 개수 증가
    }
}

// 유클리디안 거리 계산
double euclidean_distance(int x1, int y1, int x2, int y2) {
    return sqrt(1.0 * (x1 - x2) * (x1 - x2) + 1.0 * (y1 - y2) * (y1 - y2));
}

void input() {
    cin >> N >> M;
    
    for (int i = 1; i <= N; i++) {
        parent[i] = i;
        cin >> god[i].first >> god[i].second;
    }

    // 이미 연결된 간선 처리
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        if (find(u) != find(v)) {
            union_sets(u, v);
        }
    }

    // 모든 노드 쌍의 유클리드 거리 계산 후 간선 추가
    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            double dist = euclidean_distance(god[i].first, god[i].second, god[j].first, god[j].second);
            edges.push_back({i, j, dist});
        }
    }
}

void kruskal() {
    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.weight < b.weight;
    });

    for (const auto &edge : edges) {
        if (find(edge.u) != find(edge.v)) {
            union_sets(edge.u, edge.v);
            result += edge.weight;
            if (cnt == N - 1) break;  // MST가 완성되면 종료
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    input();
    kruskal();

    cout << fixed << setprecision(2) << result << "\n";
    return 0;
}
