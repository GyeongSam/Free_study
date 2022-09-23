#include <iostream>
#include <vector>
struct m {
	int I;
	int J;
	int A;
	int D;
};

int di[5] = { 0,-1,1,0,0 }, dj[5] = { 0,0,0,-1,1 };
int X[5] = { 0, 2, 1, 4, 3 };


int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N, M, K;
		scanf("%d", &N, &M, &K);
		m cell[10000];
		std::vector<m> V;
		for (int k = 0; k < K; ++k) {
			scanf("%d %d %d %d", &cell[k].I, &cell[k].J, &cell[k].A, &cell[k].D);
		}

		while (N--) {
			int cnt[100][100] = { 0, };
			for (int k = 0; k < K; ++k) {
				
				if (cell[k].A) {
					cell[k].I = cell[k].I + di[cell[k].D];
					cell[k].J = cell[k].J + dj[cell[k].D];
					
					cnt[cell[k].I][cell[k].J] += 1;


				}

			}

		}
		

	}
}
