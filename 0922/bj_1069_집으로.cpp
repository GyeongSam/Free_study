#include <iostream>
#include <cmath>
int main() {
	int X, Y, D, K;
	double ans = 0, case2 = 0, case3=0;
	scanf("%d %d %d %d", &X, &Y, &D, &K);
	double d = pow(pow(X, 2) + pow(Y, 2), 0.5);
	int N = (int) d / D;
	
	ans = N * K + d - N * D;
	case2 = (N + 1)*K + (N+1)*D-d;
	if (N) case3 = (N + 1)*K;
	else case3 = 2 * K;
	if (case2 < ans) ans = case2;
	if (case3 < ans) ans = case3;
	printf("%.13f", ans);
}