#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

int min = 1000;

int FD(int parents[],int x) {
	while (x != parents[x]) {
		x = parents[x];
	}
	return x;
}
void UN(int parents[], int a, int b) {
	parents[FD(parents, b)] = FD(parents, a);
}


void dfs(int n, int cnt, int (*edges)[11], int selected, int& N, int pp[]) {

	if (cnt > N / 2) return;

	int parents[11],pc[11]={0,};
	for (int x = 1; x <= N; ++x) parents[x] = x;
	for (int i = 1; i < N; ++i) {
		for (int j = i + 1; j <= N; ++j) {
			if (edges[i][j] && (((selected & (1 << i))>0) == ((selected & (1 << j))>0))) {
				UN(parents, i, j);
			}
		}
	}
	for (int x = 1; x <= N; ++x) pc[FD(parents, x)] = 1;
	int ok=0;
	for (int x = 1; x <= N; ++x) ok += pc[x];
	if (ok == 2) {

		int c1 = 0, c2 = 0, ans;
		for (int i = 1; i <= N; ++i) {
			if (selected & (1 << i)) c1 += pp[i];
			else c2 += pp[i];

		}
		if (c1 > c2) ans = c1 - c2;
		else ans = c2 - c1;
		if (ans < min) min = ans;
	}

	for (int i = n + 1; i <= N; ++i) {
		dfs(i, cnt+1, edges, selected|(1 << i) , N, pp);
	}
}

int main() {
	int N,pp[11],edges[11][11]={0,};
	int selected=0;
	
	scanf("%d", &N);
	for (int i = 1; i <= N; ++i) scanf("%d", &pp[i]);
	for (int s = 1; s <= N; ++s) {
		int n,e;
		scanf("%d", &n);
		while (n--) {
			scanf("%d", &e);
			edges[s][e] = 1;
			edges[e][s] = 1;
		}
	}
	dfs(0, 0, edges, selected, N, pp);
	if (min == 1000) printf("-1");
	else printf("%d\n", min);
}