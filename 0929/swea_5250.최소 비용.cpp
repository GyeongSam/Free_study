#include <iostream>
#include <queue>
#define INF 1e10;

int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };

struct E {
	int V;
	int i;
	int j;
	E(int a, int b, int c) {
		V = a;
		i = b;
		j = c;
	}
	bool operator<(const E &b)const {
		return V > b.V;
	}
};

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		std::priority_queue <E> PQ;
		int N, i, j;
		int H[100][100];
		int DP[100][100];
		scanf("%d", &N);
		for (i = 0; i < N; ++i) {
			for (j = 0; j < N; ++j) {
				scanf("%d", &H[i][j]);
				DP[i][j] = INF;
			}
		}
		DP[0][0] = 0;
		PQ.emplace(0, 0, 0);

		while (1) {
			E q = PQ.top();
			if ((q.i == N - 1) && (q.j == N - 1)) break;
			PQ.pop();
			for (int d = 0; d < 4; ++d) {
				int I = q.i + di[d], J = q.j + dj[d];
				if (I < 0 || I >= N || J < 0 || J >= N) continue;
				int V = (H[I][J] > H[q.i][q.j]) ? (H[I][J] - H[q.i][q.j] + 1) : 1;
				if (DP[I][J] > q.V + V) {
					DP[I][J] = q.V + V;
					PQ.emplace(DP[I][J], I, J);
				}
			}
		}

		printf("#%d %d\n", t, DP[N - 1][N - 1]);
	}
}