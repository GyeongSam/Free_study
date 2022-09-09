#include <iostream>
using namespace std;

int di[4] = {-1,0,1,0};
int dj[4] = {0,1,0,-1};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int L[101][101]{};
	int N, M, K, I, J, R, min=10000;
	cin >> N >> M >> K;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> L[i][j];
		}
	}
	while (K--) {
		cin >> I >> J >> R;
		for (int r = 1; r <= R; r++) {
			int Is = I - r;
			int Js = J - r;
			int temp = L[Is][Js];
			for (int d = 0; d < 4; d++) {
				for (int a = 0; a < 2*r; a++) {
					L[Is][Js]=L[Is + di[d]][Js + dj[d]];
					Is += di[d];
					Js += di[d];
				}
			}
			L[Is][Js + 1] = temp;

			cout << "ÀÌ¹ר r" << r << "\n";
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= M; j++) {
					cout << L[i][j] << " ";
				}
				cout << "\n";
		}
	}


	}

}