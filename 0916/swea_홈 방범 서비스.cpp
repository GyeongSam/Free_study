#include <iostream>

int T,N,M,MAX;
int cost_by[21][21][43];
int need[43];
bool home[21][21];


void setting(int I,int J) {
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			for (int k = abs(J - j) + abs(I - i) + 1; k < 43; ++k) {
				++cost_by[i][j][k];
			}
		}
	}
}

int main() {
	scanf("%d", &T);

	for (int k = 1; k < 43; ++k) {
		need[k] = k * k + (k - 1)*(k - 1);
	}


	for (int t = 1; t <= T; ++t) {
		MAX = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				for (int h = 0; h < 43; ++h) {
					cost_by[i][j][h] = 0;
				}
			}
		}

		scanf("%d %d", &N, &M);

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &home[i][j]);
				if (home[i][j]) setting(i, j);
			}
		}

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				for (int k = 1; k < 43; ++k) {
					if (need[k] < M*cost_by[i][j][k] && cost_by[i][j][k]>MAX) {
						MAX = cost_by[i][j][k];
					}
				}
			}
		}
		
		printf("#%d %d\n",t, MAX);


	}
}