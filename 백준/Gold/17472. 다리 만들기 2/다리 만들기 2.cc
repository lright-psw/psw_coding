#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cstring>
using namespace std;

const int MAX_N = 11;

// 상 하 좌 우
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 }; 

struct Edge {
    int from, to, distance;
};

int N, M;
int map[MAX_N][MAX_N];
int parent[MAX_N];
vector<Edge> v;

int island = 1;


void input() {
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 1) {
                map[i][j] = -1;
            }
        }
    }
}

//파인드
int find(int x) {
    if (x == parent[x]) {
        return x;
    }
    return parent[x] = find(parent[x]);
}

//유니온
void setunion(int a, int b) {
    a = find(a);
    b = find(b);
    if (a < b) {
        parent[b] = a;
    }
    else {
        parent[a] = b;
    }
}

// 섬 구분
void bfs(int y, int x, int idx) {
    deque<pair<int,int>> dq;
    dq.push_back({ x, y });
    map[y][x] = idx;
    while (!dq.empty()) {
        int x = dq.front().first;
        int y = dq.front().second;
        dq.pop_front();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= M || ny < 0 || ny >= N)
                continue;
            if (map[ny][nx] == -1) {
                map[ny][nx] = idx;
                dq.push_back({ nx ,ny });
            }
        }
    }
}

// 섬마다 최소 거리 계산
void find_distance(int y, int x, int dir) {
    int sum = 0;
    int island_number = map[y][x];
    int nx = x;
    int ny = y;
    while (1) {
        nx += dx[dir];
        ny += dy[dir];
        if (nx < 0 || nx >= M || ny < 0 || ny >= N)
            return;
        if (map[ny][nx] == 0) {
            sum += 1;
        }
        else {
            if (sum >= 2) {
                v.push_back({ island_number, map[ny][nx], sum });
            }
            return;
        }
    }
}

bool compareEdge(const Edge& a, const Edge& b) {
    return a.distance < b.distance;
}

// MST 알고리즘
void kruskal() {
    int sum = 0;
    int count = 0;

    sort(v.begin(), v.end(), compareEdge);
    for (int i = 0; i <= MAX_N; i++)
    {
        parent[i] = i;
    }

    island -= 1;

    for (int i = 0; i < v.size(); i++)
    {
        int from = v[i].from;
        int to = v[i].to;
        int cost = v[i].distance;

        if (find(from) != find(to)) {
            setunion(from, to);
            sum += cost;
            count += 1;

            if (count == island - 1) {
                cout << sum;
                return;
            }
        }
    }
    cout << -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    input();

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (map[i][j] == -1) {
                bfs(i, j, island);
                island += 1;
            }
        }
    }
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            for (int d = 0; d < 4; d++)
            {
                if (map[i][j] > 0) {
                    find_distance(i, j, d);
                }
            }
        }
    }

    kruskal();

    return 0;
}
