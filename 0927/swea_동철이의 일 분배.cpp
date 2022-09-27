#include <iostream>


int N;
double MAX;
bool visit[16];
int P[16][16];

void BT(int n,double p) {
	if (n == N) {
		if (p > MAX)MAX = p;
	}
	else if (MAX > p) return;
	for (int i = 0; i < N; ++i) {
		if (!visit[i]) {
			visit[i] = 1;
			BT(n + 1, p*P[n][i] / 100);
			visit[i] = 0;
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N;
		MAX = 0;
		scanf("%d",&N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &P[i][j]);
			}
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				printf("%d ", P[i][j]);
			}
			printf("\n");
		}

		BT(0,1);
		printf("%.6f",MAX);
	}
}