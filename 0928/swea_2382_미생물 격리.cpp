#include <iostream>

int di[5] = { 0,-1,1,0,0 };
int dj[5] = { 0,0,0,-1,1 };
int RD[5] = { 0,2,1,4,3 };

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N, M, K,i,j,sum=0;
		scanf("%d %d %d", &N, &M, &K);
		int cell[100][100][3][2] = { 0, };
		while (K--) {
			scanf("%d %d", &i, &j);
			scanf("%d %d", &cell[i][j][0][0], &cell[i][j][1][0]);
		}
		bool now = 0;

		while (M--) {
			bool next = 1 - now;
			for (int i = 0; i < N; ++i) {
				for (int j = 0; j < N; ++j) {
					if (cell[i][j][0][now]) {
						int I = i + di[cell[i][j][1][now]], J = j + dj[cell[i][j][1][now]];

						cell[i][j][2][now] = cell[i][j][0][now];
						
						if (I == 0 || I == N - 1 || J == 0 || J == N - 1) {
							cell[I][J][0][next] = cell[i][j][0][now]/2;
							cell[I][J][1][next] = RD[cell[i][j][1][now]];
							cell[I][J][2][next] = cell[i][j][2][now]/2;
						}
						else if (cell[I][J][0][next]) {
							cell[I][J][0][next] += cell[i][j][0][now];
							if (cell[I][J][2][next] < cell[i][j][2][now]) {
								cell[I][J][2][next] = cell[i][j][2][now];
								cell[I][J][1][next] = cell[i][j][1][now];
							}
						}
						else {
							cell[I][J][0][next] = cell[i][j][0][now];
							cell[I][J][1][next] = cell[i][j][1][now];
							cell[I][J][2][next] = cell[i][j][2][now];
						}
						cell[i][j][0][now]=0;
						cell[i][j][1][now]=0;
						cell[i][j][2][now]=0;
					}
				}
			}
			now = next;
		}

		for (int i = 0; i < N; ++i) {
				for (int j = 0; j < N; ++j) {
					sum += cell[i][j][0][now];
				}
			}
		printf("#%d %d\n", t, sum);

	}
}