//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <vector>
//
//void BT(std::vector<int> edges[],int b_t[],int e, int sum, int *MAX) {
//	if (edges[e].empty()) {
//		if (sum > *MAX) *MAX = sum;
//	}
//	else {
//		for (int i = 0; i < edges[e].size(); ++i) {
//			BT(edges, b_t, edges[e][i], sum + b_t[edges[e][i]], MAX);
//		}
//	}
//
//}
//int main() {
//	int T;
//	scanf("%d", &T);
//	while (T--) {
//		int N, K, b_t[1001], s, e, end, MAX=0;
//		std::vector <int> edges[1001];
//		scanf("%d %d", &N, &K);
//		for (int n = 1; n <= N; ++n) scanf("%d", &b_t[n]);
//		while (K--) {
//			scanf("%d %d", &s, &e);
//			edges[e].push_back(s);
//		}
//		scanf("%d", &end);
//		BT(edges, b_t, end, b_t[end], &MAX);
//		printf("%d\n", MAX);
//	}
//
//}