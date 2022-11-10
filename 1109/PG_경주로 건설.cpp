#include <iostream>


#include <string>
#include <vector>

using namespace std;

int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };
int N;
int N_;
vector <vector<bool>> visit;
int min_value = 1e9;
vector<vector<int>> board;

void dfs(int i, int j, int d, int sum) {
	if (i == N_ && j == N_) {
		if (sum < min_value) min_value = sum;
		return;
	}
	if (sum >= min_value - (2*N-i-j-2)*100) return;
	for (int c = 0; c < 4; ++c) {
		if (r[c] == d)continue;
		int ni = i + di[c], nj = j + dj[c];
		if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;
		if (!board[ni][nj] && !visit[ni][nj]) {
			visit[ni][nj] = 1;
			if (c == d) dfs(ni, nj, c, sum + 100);
			else dfs(ni, nj, c, sum + 600);
			visit[ni][nj] = 0;
		}
	}
}

int solution(vector<vector<int>> temp_board) {
	int answer = 0;
	N = temp_board.size();
	N_ = N - 1;
	board.resize(N, vector<int>(N, 0));
	for (int i = 0; i < N; ++i) {
		for (int j=0; j<N;++j){
		board[i][j] = temp_board[i][j];
		}
	}
	visit.resize(N, vector<bool>(N, 0));
	dfs(0, 0, 5, 0);
	answer = min_value - 500;
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

//
//
//#include <string>
//#include <vector>
//#include <queue>
//
//using namespace std;
//
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };
//
//struct state {
//	int i, j, d;
//};
//
//int solution(vector<vector<int>> board) {
//	int answer = 0;
//
//	vector<vector<int>> value;
//	int N = board.size();
//	value.resize(N, vector<int>(N, 1e9));
//	queue<state> Q;
//	Q.push({ 0, 1, 1 });
//	Q.push({ 1, 0, 0 });
//	value[0][1] = 100;
//	value[1][0] = 100;
//	while (!Q.empty()) {
//
//
//		state a = Q.front();
//
//
//		printf("pop: %d %d %d\n", a.i, a.j, a.d);
//
//		for (int i = 0; i < N; ++i) {
//			for (int j = 0; j < N; ++j) {
//				if (value[i][j] == 1e9) printf("INF ");
//				else printf("%d ", value[i][j]);
//			}
//			printf("\n");
//		}
//		printf("\n");
//
//
//		Q.pop();
//
//		for (int d = 0; d < 4; ++d) {
//
//			int ni = a.i + di[d], nj = a.j + dj[d];
//
//			printf("Å½»ö:%d %d\n", ni, nj);
//			if (r[d] == a.d || ni < 0 || ni >= N || nj < 0 || nj >= N || board[ni][nj])continue;
//			int v;
//			v = ((d == a.d) ? 100 : 600);
//			printf("%d\n", v);
//			if (value[a.i][a.j] + v < value[ni][nj]) {
//				value[ni][nj] = value[a.i][a.j] + v;
//				Q.push({ ni, nj, d });
//				printf("push: %d %d %d\n", ni, nj, d);
//			}
//		}
//	}
//
//
//
//
//	answer = value[N - 1][N - 1];
//	return answer;
//}

//
//
//#include <string>
//#include <vector>
//#include <queue>
//#define INF 1e9
//
//using namespace std;
//
//int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 }, r[4] = { 2,3,0,1 };
//
//struct state {
//	int i, j, d;
//};
//
//int min(int a, int b) {
//	if (a > b) return b;
//	return a;
//}
//
//int solution(vector<vector<int>> board) {
//	int answer = 0;
//
//	vector<vector<vector<int>>> value;
//	int N = board.size();
//	value.resize(N, vector<vector<int>>(N, vector<int>(4, INF)));
//	queue<state> Q;
//	Q.push({ 0, 1, 1 });
//	Q.push({ 1, 0, 0 });
//	value[0][1][1] = 100;
//	value[1][0][0] = 100;
//
//	while (!Q.empty()) {
//		state a = Q.front();
//
//
//		//printf("pop: %d %d %d\n", a.i, a.j, a.d);
//
//		//for (int i = 0; i < N; ++i) {
//		//	for (int j = 0; j < N; ++j) {
//		//		printf("(");
//		//		for (int d = 0; d < 4; ++d) {
//		//			if (value[i][j][d] == INF) {
//		//				printf("INF ");
//		//			}
//		//			else printf("%d ", value[i][j][d]);
//		//		}
//		//		printf(") ");
//		//	}
//		//	printf("\n");
//		//}
//		//printf("\n");
//
//
//		Q.pop();
//
//		for (int d = 0; d < 4; ++d) {
//
//			int ni = a.i + di[d], nj = a.j + dj[d];
//
//			//printf("Å½»ö:%d %d\n", ni, nj);
//			if (ni < 0 || ni >= N || nj < 0 || nj >= N || board[ni][nj])continue;
//
//			int case1 = value[a.i][a.j][0] + ((d == 0) ? 100 : 600);
//			int case2 = value[a.i][a.j][1] + ((d == 1) ? 100 : 600);
//			int case3 = value[a.i][a.j][2] + ((d == 2) ? 100 : 600);
//			int case4 = value[a.i][a.j][3] + ((d == 3) ? 100 : 600);
//			int v = min(case1, min(case2, min(case3, case4)));
//			if (value[ni][nj][d] > v) {
//				value[ni][nj][d] = v;
//				Q.push({ ni, nj, d });
//			}
//		}
//	}
//	answer = min(value[N - 1][N - 1][0], min(value[N - 1][N - 1][1], min(value[N - 1][N - 1][2], value[N - 1][N - 1][3])));
//	return answer;
//}