#include <iostream>
#include <queue>

using namespace std;

struct axis {
	int i;
	int j;
};

int forest[500][500];
int dp[500][500];
bool visit[500][500];
int N,M=0;
int di[4] = { 1,0,-1,0 }, dj[4] = { 0,1,0,-1 };
queue <axis> S;
axis sub, ssub, x;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	sub.i = 0;
	sub.j = 0;
	S.push(sub);
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			cin >> forest[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			dp[i][j] = 1;
		}
	}

	while (!S.empty()) {
		sub = S.front();
		/*cout << sub.i<<" "<< sub.j<<"\n";*/
		S.pop();
		for (int d = 0; d < 4; ++d) {
			x.i = sub.i + di[d];
			x.j = sub.j + dj[d];
			if (x.i >= 0 && x.i < N && x.j >= 0 && x.j < N) {
				if (forest[sub.i][sub.j] > forest[x.i][x.j] && dp[sub.i][sub.j] < dp[x.i][x.j] + 1) {
					dp[sub.i][sub.j] = dp[x.i][x.j] + 1;
					if (dp[sub.i][sub.j] > M)M = dp[sub.i][sub.j];
					for (int dd = 0; dd < 4; ++dd) {
						ssub.i = sub.i + di[dd];
						ssub.j = sub.j + dj[dd];
						if (ssub.i >= 0 && ssub.i < N && ssub.j >= 0 && ssub.j < N && forest[ssub.i][ssub.j]>forest[sub.i][sub.j]) {
							S.push(ssub);
							/*cout << "스택에 넣는다" << ssub.i << " " << ssub.j << "\n";*/
							visit[ssub.i][ssub.j] = 1;
						}
					}
				}
				if (visit[x.i][x.j] == 0) { S.push(x); visit[x.i][x.j] = 1; }
			}
		}
	}
	cout << M << "\n";
	/*for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << dp[i][j] << " ";
		}
		cout << "\n";
	}*/

}