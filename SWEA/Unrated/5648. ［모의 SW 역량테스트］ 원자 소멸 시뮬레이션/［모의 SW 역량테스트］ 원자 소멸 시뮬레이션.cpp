#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int T;
int N;

// 상 하 좌 우
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int map[4001][4001];

struct ATOM{
	int x, y;
	int diration;
	int energy;
};
vector<ATOM> atom;
int total_energy = 0;

// 입력 함수
void input() {
	cin >> N;
	atom.clear();
	memset(map, 0, sizeof(map));
	for (int i = 0; i < N; i++)
	{
		ATOM tmp;
		cin >> tmp.x >> tmp.y >> tmp.diration >> tmp.energy;
		tmp.x = (tmp.x + 1000) * 2;
		tmp.y = (tmp.y + 1000) * 2;
		atom.push_back(tmp);
	}
}

void move_atom() {
	
	while (!atom.empty()) {
		// 원자 움직이기 & 값 바꾸기
		for (int i = 0; i < atom.size(); i++)
		{
			map[atom[i].y][atom[i].x] = 0;
			int nx = atom[i].x + dx[atom[i].diration];
			int ny = atom[i].y + dy[atom[i].diration];
			// 만약 원자가 범위 밖으로 나갔다면 원자 삭제 = 에너지 없애기
			if (ny < 0 || ny > 4000 || nx < 0 || nx > 4000) {
				atom[i].energy = 0;
				continue;
			}
			//원자 이동
			atom[i].x = nx;
			atom[i].y = ny;
			// 위치 변경 = 맵 값에 에너지 추가
			map[ny][nx] += atom[i].energy;

		}
		// 충돌 확인 & 에너지 제거
		for (int i = 0; i < atom.size(); i++)
		{
			// 에너지가 0임
			if (atom[i].energy == 0) {
				continue;
			}
			// 에너지가 원자의 에너지와 다르면
			// 해야 할거 중복 제거, 에너지 제거, 답에 값 추가
			if (map[atom[i].y][atom[i].x] != atom[i].energy) {
				total_energy += map[atom[i].y][atom[i].x];
				map[atom[i].y][atom[i].x] = 0;
				atom[i].energy = 0;
			}
		}
		// 남은 원자 찾기
		vector<ATOM> tmp;
		tmp.clear();
		tmp.assign(atom.begin(), atom.end());
		atom.clear();
		for (int i = 0; i < tmp.size(); i++)
		{
			if (tmp[i].energy > 0) {
				atom.push_back(tmp[i]);
			}
		}
	}
}



int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		total_energy = 0;
		input();
		move_atom();
		cout << "#" << t << " " << total_energy << "\n";
	}
	return 0;
}
