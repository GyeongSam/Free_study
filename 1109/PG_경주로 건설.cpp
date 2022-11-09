#include <iostream>



#include <string>
#include <vector>

using namespace std;

int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };

struct state{
	int i, j, d, value;
};


int solution(vector<vector<int>> board) {
    int answer = 0;

	vector<vector<bool>> visit;
	vector<state> stack;

	stack.emplace_back(0, 0, 5, 0);
    return answer;
}

int main() {
	printf("%d", solution({ {0,0,0,0,0,0,0,1},{0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0},{0,0,0,0,1,0,0,0},{0,0,0,1,0,0,0,1},{0,0,1,0,0,0,1,0},{0,1,0,0,0,1,0,0},{1,0,0,0,0,0,0,0} }));
}

//
//#include <iostream>
//
//
//
//#include <string>
//#include <vector>
//
//using namespace std;
//
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };
//int N;
//vector <vector<int>> dp;
//vector <vector<bool>> visit;
//int min_value = 1e9;
//
//
//int min(int a, int b) {
//	if (a > b)return b;
//	return a;
//}
//
//
//int dfs(int i, int j, int d, int sum, vector<vector<int>> board) {
//	if (i == N - 1 && j == N - 1) return 0;
//	if (sum > min_value) return;
//	for (int c = 0; c < 4; ++c) {
//		if (r[c] == d)continue;
//		int ni = i + di[c], nj = j + dj[c];
//		if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;
//		if (!board[ni][nj] && !visit[ni][nj]) {
//			visit[ni][nj] = 1;
//			if (c == d) dfs(ni, nj, c, sum + 100, board);
//			else dfs(ni, nj, c, sum + 600, board);
//			visit[ni][nj] = 0;
//		}
//	}
//}
//
//int solution(vector<vector<int>> board) {
//	int answer = 0;
//	N = board.size();
//	visit.resize(N, vector<bool>(N, 0));
//	dp.resize(N, vector<int>(N, -1));
//	dfs(0, 0, 5, 0, board);
//	answer = min_value - 500;
//	return answer;
//}
//
//
//int main() {
//	printf("%d", solution({ {0,0,0,0,0,0,0,1},{0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0},{0,0,0,0,1,0,0,0},{0,0,0,1,0,0,0,1},{0,0,1,0,0,0,1,0},{0,1,0,0,0,1,0,0},{1,0,0,0,0,0,0,0} }));
//}
//
////
//#define INF 1e9
//
//
//using namespace std;
//
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };
//int N;
//vector <vector<vector<int>>> dp;
//
//int min(int a, int b) {
//	if (a > b)return b;
//	return a;
//}
//
//int dfs(int i, int j, int d, vector<vector<int>> board) {
//	if (i == N - 1 && j == N - 1) return 0;
//	int &ret = dp[i][j][d];
//	printf("%d %d %d %d\n", i, j, d, dp[i][j][d]);
//	if (ret != INF) return ret;
//	ret = 1e8;
//	for (int c = 0; c < 4; ++c) {
//		int ni = i + di[c], nj = j + dj[c];
//		if (ni < 0 || ni >= N || nj < 0 || nj >= N || board[ni][nj]) continue;
//		ret = min(ret, dfs(ni, nj, c, board) + ((d == c) ? 100 : 600));
//	}
//	return ret;
//}
//
//int solution(vector<vector<int>> board) {
//	int answer = 0;
//	N = board.size();
//	dp.resize(N, vector<vector<int>>(N, vector<int>(4, INF)));
//	answer = dfs(0, 0, 0, board);
//
//	printf("%d\n", answer);
//
//	dp.clear();
//
//	dp.resize(N, vector<vector<int>>(N, vector<int>(4, INF)));
//
//	answer = min(answer, dfs(0, 0, 1, board));
//
//	printf("%d\n", answer);
//
//	return answer;
//}
//
//
//int main() {
//	printf("%d", solution({ {0,0,0,0,0,0,0,1},{0,0,0,0,0,0,0,0},{0,0,0,0,0,1,0,0},{0,0,0,0,1,0,0,0},{0,0,0,1,0,0,0,1},{0,0,1,0,0,0,1,0},{0,1,0,0,0,1,0,0},{1,0,0,0,0,0,0,0} }));
//}