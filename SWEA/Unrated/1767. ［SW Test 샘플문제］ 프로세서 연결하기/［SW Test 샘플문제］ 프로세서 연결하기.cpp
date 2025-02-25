#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

const int MAX_N = 13;

// 상 하 좌 우
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };

int T;
int N;
int total_cpu = 0;
int minlen = 1e9;
int map[MAX_N][MAX_N];
vector<pair<int,int>> cpu;

void init() {
    N = 0;
    total_cpu = 0;
    minlen = 1e9;
    memset(map, 0, sizeof(map));
    cpu.clear();
}

void input() {
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 1) {
                if (j == 0 || j == N - 1 || i == 0 || i == N - 1)
                    continue;
                cpu.push_back({ j,i });
            }
        }
    }
}


void dfs(int depth, int wire, int cpu_count) {
    // 종료
    if (depth == cpu.size()) {
        if (cpu_count > total_cpu) {
            minlen = wire;
            total_cpu = cpu_count;
        }
        else if (cpu_count == total_cpu) {
            minlen = min(minlen, wire);
        }
        return;
    }


    // 로직
    for (int i = 0; i < 4; i++)
    {
        int nx = cpu[depth].first;
        int ny = cpu[depth].second;
        int tmp_cnt = 0;
        while (1)
        {
            nx += dx[i];
            ny += dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                break;

            if (map[ny][nx] == 1 || map[ny][nx] == 2) {
                tmp_cnt = 0;
                break;
            }
            tmp_cnt += 1;
        }

        if (tmp_cnt > 0) {
            nx = cpu[depth].first;
            ny = cpu[depth].second;
            while (1) {
                nx += dx[i];
                ny += dy[i];
                if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1)
                    break;
                map[ny][nx] = 2;
            }
            dfs(depth + 1, wire + tmp_cnt, cpu_count + 1);
            nx = cpu[depth].first;
            ny = cpu[depth].second;
            while (1) {
                nx += dx[i];
                ny += dy[i];
                if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1)
                    break;
                map[ny][nx] = 0;
            }
        }
    }
    dfs(depth + 1, wire, cpu_count);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        init();
        input();

        dfs(0, 0, 0);

        cout << "#" << test_case << " " << minlen << "\n";
    }

    return 0;
}