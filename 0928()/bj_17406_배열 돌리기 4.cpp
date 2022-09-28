#include <iostream>

struct T {
	int I;
	int J;
	int D;
};
void DFS(int n, int* MIN, int(*table)[51], T Tlist[], int visit[], int& K, int& N, int& M);
void turn(int(*table)[51], T Ta, int dir);

int main() {
	int N, M,K;
	scanf("%d %d %d", &N, &M, &K);
	int table[51][51];
	T Tlist[6];
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= M; ++j) {
			scanf("%d", &table[i][j]);
		}
	}

	int I, J, D;
	for (int k = 0; k < K;++k) {
		scanf("%d %d %d", &I, &J, &D);
		Tlist[k] = { I,J,D };
	}

	int visit[6] = { 0, };
	int MIN = 1 << 15;
	DFS(0, &MIN, table, Tlist, visit, K, N, M);
	printf("%d", MIN);
}

void DFS(int n, int* MIN, int(*table)[51], T Tlist[], int visit[], int& K, int& N, int& M) {

	if (n == K) {
		for (int i = 1; i <= N; ++i) {
			int sum = 0;
			for (int j = 1; j <= M; ++j) {
				sum += table[i][j];
			}
			if (sum < *MIN) *MIN = sum;
		}
	}
	else {
		for (int i = 0; i < K; ++i) {
			if (!visit[i]) {
				visit[i] = 1;
				turn(table, Tlist[i], 1);
				DFS(n + 1, MIN, table, Tlist, visit, K, N, M);
				turn(table, Tlist[i], -1);
				visit[i] = 0;
			}
		}
	}
}

void turn(int(*table)[51], T Ta, int dir) {

	for (int d = 1; d <= Ta.D; ++d) {
		int i = Ta.I - d, j = Ta.J - d*dir, c = 2 * d;
		int temp = table[i][j];
		while (c--) {
			table[i][j] = table[i + 1][j];
			++i;
		}
		c = 2 * d;
		while (c--) {
			table[i][j] = table[i][j + dir];
			j += dir;
		}
		c = 2 * d;
		while (c--) {
			table[i][j] = table[i - 1][j];
			--i;
		}
		c = 2 * d - 1;
		while (c--) {
			table[i][j] = table[i][j - dir];
			j -= dir;
		}
		table[i][j] = temp;
	}
}
