#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstring>
#include <string>
using namespace std;

// 상 하 좌 우
int dy[4] = { -1, 1, 0, 0 };
int dx[4] = { 0, 0, -1, 1 };
int score[5] = { 0,1,10,100,1000 };

int main()
{
    int N;
    cin >> N;

    int seat[21][21] = { 0 };
    int rst = 0;

    unordered_map<int, vector<int>> like;
    vector<int> orders;

    for (size_t i = 0; i < N * N; i++) {
        int order, l1, l2, l3, l4;
        cin >> order >> l1 >> l2 >> l3 >> l4;
        orders.push_back(order);
        like[order] = { l1, l2, l3, l4 };
    }

    // 자리배정 로직
    for (size_t idx = 0; idx < orders.size(); idx++)
    {
        int student = orders[idx];
        int max_like = -1, max_empty = -1, min_y = 10e9, min_x = 10e9;
        for (size_t y = 0; y < N; y++)
        {
            for (size_t x = 0; x < N; x++)
            {
                if (seat[y][x] != 0)
                    continue;

                int cnt = 0, empty = 0;

                for (size_t d = 0; d < 4; d++)
                {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny <0 || ny>=N || nx <0 || nx >= N)
                        continue;
                    if (seat[ny][nx] == 0) {
                        empty += 1;
                    }
                    else {
                        for (const auto& l : like[student]) {
                            if (seat[ny][nx] == l) {
                                cnt += 1;
                                break;
                            }
                        }
                    }
                }

                if (cnt > max_like || // 좋아하는 친구
                    (cnt == max_like && empty > max_empty) || // 주변이 많이 비었음
                    (cnt == max_like && empty == max_empty && y < min_y) ||// y축이 작은거 우선
                    (cnt == max_like && empty == max_empty && y == min_y && x < min_x)) // x축이 작은거 우선
                {
                    max_like = cnt;
                    max_empty =empty;
                    min_y = y;
                    min_x = x;
                }
            }
        }
        seat[min_y][min_x] = student;
    }


    //점수 계산 로직
    for (size_t i = 0; i < N; i++)
    {
        for (size_t j = 0; j < N; j++)
        {
            int tmp = seat[i][j];
            int cnt = 0;
            for (size_t d = 0; d < 4; d++)
            {
                int ny = i + dy[d];
                int nx = j + dx[d];
                if (ny < 0 || ny>=N || nx < 0 || nx >= N)
                    continue;
                for (const auto& l : like[tmp]) {
                    if (seat[ny][nx] == l) {
                        cnt += 1;
                        break;
                    }
                }
            }
            rst += score[cnt];
        }
    }

    cout << rst << endl;

    return 0;
}