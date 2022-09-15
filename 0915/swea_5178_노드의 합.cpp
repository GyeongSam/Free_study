#include <iostream>
using namespace std;

int T, N, M, L, id, value;
int tree[1001];


int call(int need) {
	cout << need << tree[need] <<"\n";
	if (need > N) return 0;
	if (tree[need]) return tree[need];
	return call(2 * need) + call(2 * need + 1);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		for (int i = 0; i < 1001; ++i) {
			tree[i] = 0;
		}
		cin >> N >> M >> L;
		for (int i = 1; i <= M; ++i) {
			cin >> id >> value;
			tree[id] = value;
		}
		cout << "#" << t <<" "<< call(L);
	}
	
}