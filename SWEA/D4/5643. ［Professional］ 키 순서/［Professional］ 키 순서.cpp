#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int T;
int N, M;
int rst = 0;
// 세로는 해당학생 가로는 다른학생과의 크기 비교 
int arr[501][501];

void init() {
    memset(arr, -1, sizeof(arr));
    rst = 0;
}

void input() {
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        //본인보다 크면 1 작으면 0
        arr[a - 1][b - 1] = 1;
        arr[b - 1][a - 1] = 0;

}
}

void find_students_hight() {
    // 타겟 학생
    for (int i = 0; i < N; i++)
    {
        // 진짜 탐색 로직
        for (int target = 0; target < N; target++)
        {
            // 본인을 본인이 모르니깐 패스
            if (i == target) {
                continue;
            }
            //탐색 로직
            else if (arr[i][target] == -1) {
                //키를 아는 다른애를 탐색해서 내가 모르는 애보다 작은지 큰지 찾아야해
                for (int k = 0; k < N; k++)
                {
                    if (arr[i][k] == 0) {
                        if (arr[k][target] == 0) {
                            arr[i][target] = 0;
                            arr[target][i] = 1;
                        }
                    }
                    else if (arr[i][k] == 1) {
                        if (arr[k][target] == 1) {
                            arr[i][target] = 1;
                            arr[target][i] = 0;
                        }
                    }
                }

        }
    }
}
for (int i = 0; i < N; i++)
{
    int tmp = 0;
    for (int j = 0; j < N; j++)
    {
        if (i == j) continue;
        if (arr[i][j] > -1) {
            tmp += 1;
        }
    }
    if (tmp == N - 1) {
        rst += 1;
    }
}
}

int main()
{
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++)
    {
        init();
        input();
        find_students_hight();
        cout << "#" << test_case << " " << rst << "\n";
    }
    return 0;
}