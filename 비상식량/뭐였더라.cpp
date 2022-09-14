#include <iostream>
using namespace std;

struct ROT {
	int I;
	int J;
	int R;
};

int di[4] = {1,0,-1,0};
int dj[4] = {0,1,0,-1};
int L[101][101]{};
int N, M, K, I, J, R, min = 10000;

ROT rot_list[6];

void BT(int c) {
	if (c == K) {

	}
}


int rot(int I, int J, int R) {
	for (int r = 1; r <= R; r++) {
		int Is = I - r;
		int Js = J - r;
		int temp = L[Is][Js];
		for (int d = 0; d < 4; d++) {
			for (int a = 0; a < 2 * r; a++) {
				L[Is][Js] = L[Is + di[d]][Js + dj[d]];
				Is += di[d];
				Js += dj[d];
			}
		}
		L[Is][Js + 1] = temp;


	}
}




int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> L[i][j];
		}
	}
	
	for (int k = 0; k < K; k++) {
		ROT sub;
		cin >> sub.I >> sub.J >> sub.R;
		rot_list[k] = sub;
	}

	
	for (int i = 1; i <= N; i++) {
		int sub = 0;
		for (int j = 1; j <= M; j++) {
			sub += L[i][j];
		}
		if (sub < min) min = sub;
	}
	
	cout << min << "\n";
	}

