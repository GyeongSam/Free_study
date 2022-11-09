//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//
//
//#include <string>
//#include <vector>
//#define F(x,X) for(int x=0;x<X;++x)
//#define F_(x,X) for(int x=X-1;x>=0;--x)
//
//using namespace std;
//
//
//
//
//
//
//
//
//bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
//	bool answer = true;
//	vector <vector<int>> select(4);
//	int M = key.size();
//	int N = lock.size();
//	int cnt_key = 0;
//	int cnt_lock = 0;
//	int c;
//	vector <int> cnt(4,0);
//	vector <pair<int, int>> move;
//	vector <vector < vector<int>>> comp(4,vector<vector<int>>(N,vector<int>(N)));
//	F(i, N) F(j, N) if (key[i][j]) cnt_key++;
//	F(i, N) F(j, N) if (!lock[i][j]) cnt_lock++;
//	
//	F(i, N)F(j, N) {
//		printf("%d %d\n", i, j);
//		comp[0][i][j] = lock[i][j];
//		comp[1][i][j] = lock[N - 1 - j][i];
//		comp[2][i][j] = lock[N - 1 - i][N - 1 - j];
//		comp[3][i][j] = lock[j][N - 1 - i];
//	}
//	F(c, 4) {
//		F(i, N) {
//			F(j, N) printf("%d ", comp[c][i][j]);
//			printf("\n");
//		}
//		printf("\n");
//	}
//
//
//
//	F(I, M) {
//		F(J, M) {
//			cnt = { 0,0,0,0 };
//			F(i, M) {
//				F(j, M) {
//					if (key[i][j]) {
//						c = 0;
//						if (i >= I) c += 2;
//						if (j >= J) c++;
//						cnt[c]++;
//					}
//				}
//			}
//			printf("%d,%d:(%d,%d,%d,%d)\n", I, J, cnt[0], cnt[1], cnt[2], cnt[3]);
//			if (cnt[0] == cnt_lock) move.emplace_back(M - I, M - J);
//			if (cnt[1] == cnt_lock) move.emplace_back(M - I, -J);
//			if (cnt[2] == cnt_lock) move.emplace_back(-I, M - J);
//			if (cnt[3] == cnt_lock) move.emplace_back(-I, -J);
//		}
//	}
//
//	for (int d = 0; d < move.size(); ++d) {
//		int di = move[d].first;
//		int dj = move[d].second;
//
//	}
//
//
//
//
//
//
//
//
//
//
//	return answer;
//}
//
//
//
//int main() {
//	solution({ {0, 0, 0}, {1, 0, 0}, {0, 1, 1} }, { {1, 1, 1}, {1, 1, 0}, {1, 0, 1} });
//}