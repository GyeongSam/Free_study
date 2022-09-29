#include <iostream>

int start(int (*info)[10], int *comb,int &N) {
	int i = 1, t=0, out_cnt=0, score=0;
	bool B[4] = { 0, };
	while (i <= N) {
		int heat = info[i][comb[t]];
		if (heat) {
			B[0] = 1;
			for (int x = 3; x >= 0; --x) {
				if (B[x]) {
					if (x + heat > 3) ++score;
					else B[x + heat] = 1;
					B[x] = 0;
				}
			}
		}
		else {
			if (++out_cnt == 3) {
				++i;
				out_cnt = 0;
				for (int x = 3; x >= 0; --x) B[x] = 0;
			}
		}
		++t %= 9;
	}
	return score;
}

void DFS(int n, int &N, int *ans, int *comb, bool *use, int (*info)[10]) {
	if (n == 8) {
		int temp = start(info, comb, N);
		if (temp > *ans) *ans = temp;
	}
	else {
		for (int i = 2; i <10 ; ++i) {
			if (!use[i]) {
				if (n > 2) {
					comb[n +1] = i;
				}
				else comb[n] = i;
				use[i] = 1;
				DFS(n + 1, N, ans, comb, use,info);
				if (n > 2) {
					comb[n + 1] = 0;
				}
				else comb[n] = 0;
				use[i] = 0;
			}
		}
	}

}


int main() {
	int N,ans;
	int info[51][10];
	int o_cnt;
	scanf("%d", &N);
	for (int n = 1; n <= N; ++n) {
		for (int t = 1; t <= 9; ++t) {
			scanf("%d", &info[n][t]);
		}
	}
	bool use[10] = { 0, };
	use[1] = 1;
	int comb[9];
	comb[3] = 1;
	DFS(0, N, &ans, comb, use, info);
	printf("%d", ans);
}