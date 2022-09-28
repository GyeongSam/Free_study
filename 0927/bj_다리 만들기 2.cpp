#include <iostream>
#include <vector>
#include <algorithm>

struct eg {
	int V;
	int S;
	int E;
};

int N, M;
int island[10][10];
int E[10][10] = { 0, };
int pr[10];
std::vector <eg> Edge;

bool comp(eg A, eg B) { return A.V < B.V; }

void setN(int i, int j, int n) {
	if (i < 0 || i >= N || j < 0 || j >= M) return;
	if (island[i][j] == 1) {
		island[i][j] = n;
		setN(i + 1, j, n);
		setN(i - 1, j, n);
		setN(i, j + 1, n);
		setN(i, j - 1, n);
	}
	else return;
}

void setB(int i, int j) {
	int I = i, J = j;
	while (++I <N) {
		if (island[I][J]) {
			if (I - i - 1 >= 2 && island[I][J] != island[i][j] && (!E[island[i][j]][island[I][J]] || E[island[i][j]][island[I][J]] > I - i - 1)) {
				E[island[i][j]][island[I][J]] = I - i - 1;
				E[island[I][J]][island[i][j]] = I - i - 1;
			}
			break;
		}
	}
	I = i, J = j;
	while (++J <M) {
		if (island[I][J]) {
			if (J - j - 1 >= 2 && island[I][J] != island[i][j] && (!E[island[i][j]][island[I][J]] || E[island[i][j]][island[I][J]] > J - j - 1)) {
				E[island[i][j]][island[I][J]] = J - j - 1;
				E[island[I][J]][island[i][j]] = J - j - 1;
			}
			break;
		}
	}
}

int main() {
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			scanf("%d", &island[i][j]);
		}
	}

	int sub = 1;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (island[i][j] == 1) {
				setN(i, j, ++sub);
			}
		}
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (island[i][j]) setB(i, j);
		}
	}



	int visit[10] = { 0, };
	for (int s = 2; s < sub; ++s) {
		for (int e = s + 1; e <= sub; ++e) {
			if (E[s][e]) {
				Edge.push_back({ E[s][e],s,e });
				visit[s] = 1;
				visit[e] = 1;
			}
		}
	}
	int cant = 0;
	for (int x = 2; x <= sub; ++x) {
		if (!visit[x]) cant = 1;
	}
	if (cant) printf("-1");
	else {
		std::sort(Edge.begin(), Edge.end(),comp);
		
		for (int x = 2; x <= sub; ++x) {
			pr[x] = x;
		}

		int sum = 0,cnt=0;

		for (int x = 0; x < Edge.size(); ++x) {
			int S = Edge[x].S, E = Edge[x].E;

			if (pr[S] == pr[E])continue;

			if (pr[E] != E) {
				if (pr[E] < S) {
					pr[S] = pr[E];
				}
				else {
					int pr_sub = pr[E];
					for (int z = 2; z <= sub; ++z) {
						if (pr[z] == pr_sub) pr[z] = S;
					}
				}
			}
			else {
				int pr_sub = pr[E];
				for (int z = 2; z <= sub; ++z) {
					if (pr[z] == pr_sub) pr[z] = S;
				}
				pr[E] = S;
				while (pr[S] != S) {
					S = pr[S];
					pr[E] = S;

				}
			}

			sum += Edge[x].V;
			++cnt;
			if (cnt == sub - 2) break;
		}
		if (cnt!=sub-2) printf("-1");
		else printf("%d", sum);

	}


}