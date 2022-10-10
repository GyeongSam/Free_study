#define _CRT_SECURE_NO_WARNINGS
#include <iostream>


int max(int a, int b) {
	if (a > b) return a;
	else return b;
}

int dfs(int n, int dd, int* wine, int* dp, int& N) {
	if (n > N-1 || dd > 2) return 0;
	if (dp[n] != -1) return dp[n];
	dp[n] = wine[n];
	dp[n] = max(dfs(n + 1, 0, wine, dp, N), dfs(n + 1, dd + 1, wine, dp, N)+wine[n]);
	return dp[n];
}

int main() {
	int N;
	int wine[10001];
	int dp[10001];
	scanf("%d", &N);
	for (int n = 0; n < N; ++n) {
		scanf("%d", &wine[n]);
		dp[n] = -1;
	}
	printf("%d",dfs(0, 0, wine, dp, N));
}