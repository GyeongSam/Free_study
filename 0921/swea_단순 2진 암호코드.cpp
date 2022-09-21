//#include <iostream>
//
//using namespace std;
//
//int T, tc,N,M,s,ss,n;
//char ip[101];
//int btoi[10][8] = { 0b0001101,0b0011001,0b0010011,0b0111101,0b0100011,0b0110001,0b0101111,0b0111011,0b0110111,0b0001011};
//int SECRET[8];
//
//bool is_valid(int* A) {
//	return !((3 * (A[0] + A[2] + A[4] + A[6]) + A[1] + A[3] + A[5] + A[7]) % 10);
//}
//
//int index() {
//	for (int x = 0; x < 10; ++x) {
//		printf("%d %d %d %d\n", x, *secret[x], *B,*secret[x] == *B);
//		if (*secret[x] ==*B) {
//			return x;
//		}
//	}
//	return -1;
//}
//
//int main() {
//	scanf("%d", &T);
//	while (++tc <= T) {
//		scanf("%d", &N, &M);
//		while (N--) {
//			scanf("%s", &ip);
//			for (s = M - 1; s >= 0; --s) {
//				if (ip[s] == '1' && s>=55) {
//					ss = s;
//					while (ss >= s - 55) {
//						ss--
//						n++;
//
//						if (n == 7) {
//
//						}
//
//					}
//
//				}
//			}
//		}
//
//	}
//	printf("%d\n",index());
//}