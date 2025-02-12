#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int T;
int N, X;
int rst = 0;
vector<vector<int>> map;



void input() {
	cin >> N >> X;
	map.assign(N, vector<int>(N, 0));
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> map[i][j];
		}
	}
}

bool check(vector<int>& line) {
	vector<int> visit(N, 0);
	for (int i = 1; i < N; i++)
	{
		if (abs(line[i] - line[i - 1]) > 1) {
			return false;
		}
		// 현재 > 이전 왼쪽
		if (line[i] > line[i - 1]) {
			for (int j = 0; j < X; j++)
			{
				// 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
				if (i - j - 1 < 0 || visit[i - j - 1] || line[i - 1] != line[i - j - 1]) {
					return false;
				}
				visit[i - j - 1] = 1;
			}
		}

		// 현재 < 이전 오른쪽	
		if (line[i] < line[i - 1]) {
			for (int j = 0; j < X; j++)
			{
				// 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
				if (i + j >= N || visit[i + j] || line[i] != line[i + j]) {
					return false;
				}
				visit[i + j] = 1;
			}
		}
	}
	return true;
}

void canRowPlaceSlope() {
	for (int i = 0; i < N; i++)
	{
		vector<int> row(N);
		for (int j = 0; j < N; j++)
		{
			row[j] = map[i][j];
		}
		if (check(row)) {
			rst += 1;
		}
	}
}

void canColPlaceSlope() {
	for (int i = 0; i < N; i++)
	{
		vector<int> col(N);
		for (int j = 0; j < N; j++)
		{
			col[j] = map[j][i];
		}
		if (check(col)) {
			rst += 1;
		}
	}
}

int main() {
	cin >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		rst = 0;
		input();
		canRowPlaceSlope();
		canColPlaceSlope();
		cout << "#" << test_case << " " << rst << "\n";
	}
	return 0;
}