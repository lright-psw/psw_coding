#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>
using namespace std;

// 가만히 위 우 하 좌
vector<int> dy = { 0, -1, 0, 1, 0 };
vector<int> dx = { 0, 0, 1, 0, -1 };

typedef struct {
	int x, y, c, p;
} BC;

typedef struct {
	int x;
	int y;
} person;

int move_info[2][101];
vector<BC> bc;
person a_spoint, b_spoint;
int rst = 0;

// 이동 함수
void move_person(person &tmp, int dir) {
	tmp.x += dx[dir];
	tmp.y += dy[dir];
}

// 충전 계산 함수
void can_charge() {
	int max_power = 0;
	vector<BC> a_BCs, b_BCs;

	// A와 B가 충전 가능한 BC 전부 찾기
	for (BC nbc : bc) {
		int tmp_calc_a = abs(a_spoint.x - nbc.x) + abs(a_spoint.y - nbc.y);
		if (tmp_calc_a <= nbc.c) {
			a_BCs.push_back(nbc);
		}
		int tmp_calc_b = abs(b_spoint.x - nbc.x) + abs(b_spoint.y - nbc.y);
		if (tmp_calc_b <= nbc.c) {
			b_BCs.push_back(nbc);
		}
	}

	// 충전량 계산
	if (a_BCs.empty() || b_BCs.empty()) {
		// B만 가능한 경우
		if (a_BCs.empty()) {
			for (BC nbc : b_BCs) {
				max_power = max(max_power, nbc.p);
			}
		}
		// A만 가능한 경우
		else {
			for (BC nbc : a_BCs) {
				max_power = max(max_power, nbc.p);
			}
		}
	}
	else {
		int tmp;
		for (BC i : a_BCs) {
			for (BC j : b_BCs) {
				if (i.x == j.x && i.y == j.y) {
					tmp = i.p;
				}
				else {
					tmp = i.p + j.p;
				}
				max_power = max(max_power, tmp);
			}
		}
	}
	rst += max_power;
}

int main() {
	int T = 0;
	cin >> T;
	int M, A;

	for (int t = 1; t <= T; t++) {
		rst = 0;
		cin >> M >> A;
		memset(move_info, 0, sizeof(move_info));
		bc.clear();

		// 이동 정보 입력
		for (int i = 1; i < M + 1; i++) {
			cin >> move_info[0][i];
		}
		for (int i = 1; i < M + 1; i++) {
			cin >> move_info[1][i];
		}
		// BC 정보 입력
		for (int i = 0; i < A; i++) {
			int x, y, c, p;
			cin >> x >> y >> c >> p;
			bc.push_back({ x, y, c, p });
		}

		// 사용자 초기 위치 설정
		a_spoint = { 1, 1 };
		b_spoint = { 10, 10 }; 

		// 처음 충전
		can_charge();

		// 이동 및 충전
		for (int i = 1; i <= M; i++) {
			move_person(a_spoint, move_info[0][i]);
			move_person(b_spoint, move_info[1][i]);
			can_charge();
		}

		// 결과 출력
		cout << "#" << t << " " << rst << "\n";
	}
	return 0;
}
