#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
#include <queue>
using namespace std;

#define MAX 20

// 상 하 좌 우
int dy[8] = { -1,1,0,0 };
int dx[8] = { 0,0,-1,1 };

int N, M;

int arr[MAX][MAX];

struct BLOCKGROUP {
    int size, rainbow, std_y, std_x;
    vector<pair<int, int>> blocks;

    bool operator<(const BLOCKGROUP& o) const {
        if (size != o.size)
            return size > o.size;
        if(rainbow != o.rainbow)
            return rainbow > o.rainbow;
        if (std_y != o.std_y)
            return std_y > o.std_y;
        return std_x > o.std_x;
    }
};

vector<BLOCKGROUP> find_groups() {
    vector<BLOCKGROUP> groups;
    bool visited[MAX][MAX] = { 0, };

    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            if (arr[y][x] <= 0 || visited[y][x])
                continue;
            int color = arr[y][x];

            queue <pair<int, int>> q;
            vector<pair<int, int>> blocks;
            bool rainbow_visited[MAX][MAX] = { 0, };
            q.push({ y,x });
            visited[y][x] = true;
            blocks.push_back({ y,x });

            int rainbow = 0;
            int std_y = y, std_x = x;

            while (!q.empty()) {
                int cy = q.front().first;
                int cx = q.front().second;
                q.pop();

                for (int d = 0; d < 4; d++) {
                    int ny = cy + dy[d];
                    int nx = cx + dx[d];
                    if (ny < 0 || ny >= N || nx < 0 || nx >= N)
                        continue;
                    if (arr[ny][nx] == -1)
                        continue;
                    if (arr[ny][nx] == color && !visited[ny][nx]) {
                        visited[ny][nx] = true;
                        q.push({ ny, nx });
                        blocks.push_back({ ny, nx });
                        if (ny < std_y || (ny == std_y && nx < std_x)) {
                            std_y = ny;
                            std_x = nx;
                        }
                    }
                    else if (arr[ny][nx] == 0 && !rainbow_visited[ny][nx]) {
                        rainbow_visited[ny][nx] = true;
                        q.push({ ny, nx });
                        blocks.push_back({ ny, nx });
                        rainbow++;
                    }
                }
            }

            if (blocks.size() >= 2) {
                groups.push_back({ (int)blocks.size(), rainbow, std_y, std_x, blocks });
            }

            for (auto& b : blocks)
                if (arr[b.first][b.second] == 0)
                    visited[b.first][b.second] = false;
        }
    }
    return groups;
}

void gravity() {
    for (int x = 0; x < N; x++)
    {
        for (int y = N-2; y >= 0; y--)
        {
            if (arr[y][x] >= 0) {
                int ny= y;
                while (ny + 1 < N && arr[ny + 1][x] == -2) {
                    arr[ny + 1][x] = arr[ny][x];
                    arr[ny][x] = -2;
                    ny++;
                }
            }
        }
    }
}

void rotate() {
    int tmp[MAX][MAX];
    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            tmp[N - 1 - x][y] = arr[y][x];
        }
    }

    for (int y = 0; y < N; y++)
    {
        for (int x = 0; x < N; x++)
        {
            arr[y][x] = tmp[y][x];
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N >> M;

    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            cin >> arr[i][j];
        }
    }

    int rst = 0;
    while (1) {
        vector<BLOCKGROUP> groups = find_groups();
        if (groups.empty())
            break;
        sort(groups.begin(), groups.end());
        BLOCKGROUP& g = groups[0];

        for (auto& b : g.blocks) 
            arr[b.first][b.second] = -2;
        rst += g.size * g.size;

        gravity();
        rotate();
        gravity();
    }

    cout << rst << endl;
    return 0;
}