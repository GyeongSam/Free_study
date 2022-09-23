//#include <iostream>
//#include <algorithm>
//
//int m;
//
//bool comp(int a, int b) { return a > b; }
//
//void BT(int sum, int n);
//
//
//
//int main() {
//	int T;
//	scanf("%d", &T);
//	for (int t = 1; t <= T; ++t) {
//		int N, B;
//		m = 1 << 18;
//		scanf("%d %d", &N, &B);
//		int s[20];
//		for (int n = 0; n < N; ++n) scanf("%d", &s[n]);
//		std::sort(s, s + N, comp);
//		BT(0, 0);
//		printf("#%d\n", m);
//	}
//}
//
//
//void BT(int sum, int n) {
//	if (sum > B) {
//		if ((sum - B) < m) m = sum - B;
//	}
//	else {
//		for (int i = n; n < N; ++n) {
//			printf("%d ", n);
//			BT(sum + s[n]);
//		}
//	}
//}