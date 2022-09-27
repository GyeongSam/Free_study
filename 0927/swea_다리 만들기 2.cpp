#include <iostream>

int N, M;
int island[10][10];
int E[10][10] = { 0, };


void setB(int i, int j) {
	int I = i, J = j;
	while (++I <N) {
		if (island[I][J]) {
			if (I - i - 1 >= 2 && island[I][J] != island[i][j] && (!E[island[i][j]][island[I][J]] || E[island[i][j]][island[I][J]] > I - i - 1)) {
				E[island[i][j]][island[I][J]] = I - i - 1;
				E[island[I][J]][island[i][j]] = I - i - 1;
			}
			break;
		}
	}
	I = i, J = j;
	while (++J <M) {
		if (island[I][J]) {
			if (J - j - 1 >= 2 && island[I][J] != island[i][j] && (!E[island[i][j]][island[I][J]] || E[island[i][j]][island[I][J]] > J - j - 1)) {
				E[island[i][j]][island[I][J]] = J - j - 1;
				E[island[I][J]][island[i][j]] = J - j - 1;
			}
			break;
		}
	}
}


int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%d", &island[i][j]);
		}
	}
	int sub = 1;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (island[i][j] == 1) {
				if (i - 1 >= 0 && island[i-1][j]) {
					island[i][j] = island[i - 1][j];
				}
				else if (j - 1 >= 0 && island[i][j-1]) {
					island[i][j] = island[i][j-1];
				}
				else island[i][j] = ++sub;
			}
		}
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			printf("%d ", island[i][j]);
		}
		printf("\n");
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (island[i][j]) setB(i, j);
		}
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			printf("%d ", E[i][j]);
		}
		printf("\n");
	}
}