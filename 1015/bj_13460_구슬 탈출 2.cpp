//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#define F(x,X) for(int x=0;x<X;++x)
//
//
//struct W {
//	int i; int j;
//};
//
//int N, M, min = 1000;
//char board[50][50];
//const char q = '.';
//W R, B;
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };
//
//void swap(char* a, char* b) {
//	char temp = *a;
//	*a = *b;
//	*b = temp;
//}
//
//
//
//
//
//W move(W a, int d) {
//	W b = { a.i + di[d], a.j + dj[d] };
//	while (board[b.i][b.j]=='.') {
//		b.i += di[d]; b.j += dj[d];
//	}
//	if (board[b.i][b.j] == 'O') {
//		b.j = -1; b.i = -1;
//	}
//	else {
//		b.i -= di[d]; b.j -= dj[d];
//	}
//	return b;
//}
//
//void dfs(int n) {
//	if (n >= min || n>=10) return;
//
//	F(d, 4) {
//		W R_temp = R;
//		W B_temp = B;
//		
//		if (R.j == B.j) {
//			if (((d == 0) && (B.i > R.i)) || ((d == 2) && (B.i < R.i))){
//				B = move(B, d);
//				if (B.i == -1) {
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//				swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//				R = move(R, d);
//				if (R.i == -1) {
//					if (n + 1 < min) min = n + 1;
//					R = R_temp;
//					B = B_temp;
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					continue;
//				}
//				else if (B.i == B_temp.i && B.j == B_temp.j && R.i == R_temp.i && R.j == R_temp.j) {
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//				swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//				dfs(n + 1);
//				swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//				swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//				R = R_temp;
//				B = B_temp;
//			}
//			else {
//				R = move(R, d);
//				if (R.i != -1) {
//					swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//					B = move(B, d);
//					if (B.i == B_temp.i && B.j == B_temp.j && R.i == R_temp.i && R.j == R_temp.j) {
//						R = R_temp;
//						B = B_temp;
//						continue;
//					}
//					if (B.i == -1) {
//						swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//						R = R_temp;
//						B = B_temp;
//						continue;
//					}
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					dfs(n + 1);
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//					R = R_temp;
//					B = B_temp;
//				}
//				else {
//					board[R_temp.i][R_temp.j] = '.';
//					B = move(B, d);
//					if (B.i != -1) {
//						if (n + 1 < min) min = n + 1;
//					}
//					board[R_temp.i][R_temp.j] = 'R';
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//			}
//		}
//		else if (B.i == R.i) {
//			if (((d == 1) && (B.j > R.j)) || ((d == 3) && (B.j < R.j))) {
//				B = move(B, d);
//				if (B.i == -1) {
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//				swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//				R = move(R, d);
//				if (R.i == -1) {
//					if (n + 1 < min) min = n + 1;
//					R = R_temp;
//					B = B_temp;
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					continue;
//				}
//				else if (B.i == B_temp.i && B.j == B_temp.j && R.i == R_temp.i && R.j == R_temp.j) {
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//				swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//				dfs(n + 1);
//				swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//				swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//				R = R_temp;
//				B = B_temp;
//
//			}
//			else {
//				R = move(R, d);
//				if (R.i != -1) {
//					swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//					B = move(B, d);
//					if (B.i == B_temp.i && B.j == B_temp.j && R.i == R_temp.i && R.j == R_temp.j) {
//						R = R_temp;
//						B = B_temp;
//						continue;
//					}
//					if (B.i == -1) {
//						swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//						R = R_temp;
//						B = B_temp;
//						continue;
//					}
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					dfs(n + 1);
//					swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//					swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//					R = R_temp;
//					B = B_temp;
//
//				}
//				else {
//					board[R_temp.i][R_temp.j] = '.';
//					B = move(B, d);
//					if (B.i != -1) {
//						if (n + 1 < min) min = n + 1;
//					}
//					board[R_temp.i][R_temp.j] = 'R';
//					R = R_temp;
//					B = B_temp;
//					continue;
//				}
//			}
//		}
//		else {
//		B = move(B, d);
//		if (B.i == -1) {
//			R = R_temp;
//			B = B_temp;
//			continue;
//		}
//		swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//		R = move(R, d);
//		if (R.i == -1) {
//			if (n + 1 < min) min = n + 1;
//			R = R_temp;
//			B = B_temp;
//			swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//			continue;
//		}
//		else if (B.i == B_temp.i && B.j == B_temp.j && R.i == R_temp.i && R.j == R_temp.j) {
//			R = R_temp;
//			B = B_temp;
//			continue;
//		}
//		swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//		dfs(n + 1);
//		swap(&board[R.i][R.j], &board[R_temp.i][R_temp.j]);
//		swap(&board[B.i][B.j], &board[B_temp.i][B_temp.j]);
//		R = R_temp;
//		B = B_temp;
//		}
//	}
//
//}
//
//
//
//
//
//int main() {
//	scanf("%d %d", &N, &M);
//	F(n,N) scanf("%s", board[n]);
//	F(i, N)F(j, M) {
//		if (board[i][j] == 'B') {
//			B.i = i;
//			B.j = j;
//		}
//		else if (board[i][j] == 'R') {
//			R.i = i;
//			R.j = j;
//		}
//	}
//
//	dfs(0);
//	if (min == 1000) min = -1;
//	printf("%d\n", min);
//}