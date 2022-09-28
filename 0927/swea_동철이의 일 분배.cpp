#include <iostream>
int N;
double MAX;
bool visit[17];
double P[17][17];

void BT(int n,double p) {
	if (n == N) {
		if (p > MAX)MAX = p;
	}
	if (MAX >= p) return;
	for (int i = 0; i < N; ++i) {
		if (!visit[i]) {
			visit[i] = 1;
			BT(n + 1, p*P[n][i]);
			visit[i] = 0;
		}
	}
}
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d",&N);
		int sub;
		MAX = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%d", &sub);
				P[i][j] =(double) sub / 100;
			}
		}
		BT(0,1);
		printf("#%d %.6f\n",t,MAX*100);
	}
}