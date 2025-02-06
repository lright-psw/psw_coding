#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <climits>
#include <string>
#include <cstring>
#include <map>
using namespace std;

// 전역 변수
int T = 0;
int N, M, K; // 셀, 시간, 미생물수
int sum = 0;

// 상 하 좌 우
vector<int> dx = { 0,0,-1,1 };
vector<int> dy = { -1,1,0,0 };

struct BIO {
	int x, y, c, d;
};

vector<BIO> bio;

//디버그용
void print_bio() {
	for (BIO b : bio) {
		cout << " |x : " << b.x << " |y : " << b.y << " |개수 : " << b.c << " |방향 : " << b.d << "\n";
	}
}

/*로직*/

//초기화
void init() {
	bio.clear();
}

//입력
void input() {
	cin >> N >> M >> K;
	bio.resize(K);
	for (int j = 0; j < K; j++) {
		int x, y, c, d;
		cin >> x >> y >> c >> d;
		bio[j] = { x, y, c, d };
	}
}

// 방향 전환
int reverse_dir(int d) {
	if (d == 1) return 2;
	else if (d == 2) return 1;
	else if (d == 3) return 4;
	else if (d == 4) return 3;
}

// 미생물 이동
void bio_move(BIO& b) {
	b.x = b.x + dy[b.d - 1];
	b.y = b.y + dx[b.d - 1];
}

int simulate_bio() {
	for (int i = 0; i < M; i++)
	{
		map<pair<int, int>, vector<BIO>> new_bio;

		for (BIO& b : bio) {
			bio_move(b);

			if (b.x == 0 || b.y == 0 || b.x == N - 1 || b.y == N - 1) {
				b.c /= 2;
				b.d = reverse_dir(b.d);
			}

			if (b.c > 0) {
				new_bio[{b.x, b.y}].push_back(b);
			}
		}
		bio.clear();
		for (auto& it : new_bio) {
			vector<BIO>& group = it.second;
			if (group.size() > 1) {
				sort(group.begin(), group.end(), [](BIO a, BIO b) { return a.c > b.c; });
				int total_c = 0;
				int new_d = group[0].d;
				for (BIO& b : group) total_c += b.c;
				bio.push_back({ it.first.first, it.first.second, total_c, new_d });
			}
			else {
				bio.push_back(group[0]);
			}
		}
	}
	int sum = 0;
	for (BIO& b : bio)
		sum += b.c;
	return sum;
}


int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		init();
		input();
		int rst = simulate_bio();
		cout << "#" << t << " " << rst << "\n";
	}
	return 0;
}