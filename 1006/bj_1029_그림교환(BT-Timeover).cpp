#include <iostream>

int MAX=0;

void dfs(int (*cost)[15],int a, int value, int cnt, int visit ,int&N) {
	if (cnt > MAX) MAX = cnt;
	for (int b = 0; b < N; ++b) {
		if (!(visit&(1 << b))&&(cost[a][b]>=value)) {
			dfs(cost, b, cost[a][b], cnt + 1, visit | (1 << b), N);
		}
	}

}

int main() {
	int N, cost[15][15];
	char temp[16];
	scanf("%d", &N);
	for (int i = 0; i < N; ++i) {
		scanf("%s", &temp);
		for (int j = 0; j < N; ++j) {
			cost[i][j] = temp[j] - '0';
		}
	}
	dfs(cost, 0, 0, 1, 1, N);
	printf("%d", MAX);
}