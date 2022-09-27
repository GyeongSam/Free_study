//#include <iostream>
//
//
//int main() {
//	int T;
//	for (int t = 1; t <= T; ++t) {
//		int N, M;
//		scanf("%d %d", &N, &M);
//		int cnt = 0;
//		int sub;
//		int A[500000];
//		for (int n = 0; n < N; ++n) scanf("%d", &A[n]);
//		for (int n = 0; n < M; ++n) {
//			scanf("%d", &sub);
//			int l = 0, r = N-1;
//			while (l <= r) {
//				int m = (l + r) / 2;
//				if (A[m] == sub) break;
//				else if (A[m] < sub) {
//					l = m + 1;
//				}
//				else if (A[m] > sub) {
//					r = m - 1;
//				}
//			}
//
//
//		}
//
//
//
//
//	}
//}