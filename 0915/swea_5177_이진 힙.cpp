#include <iostream>
using namespace std;

int T, N, sum, tree[501] = { 0, };

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void tree_sort(int i) {
	while (1 <= i / 2 && tree[i / 2] > tree[i]) {
		swap(tree[i / 2], tree[i]);
		i /= 2;
	}
}

int main() {
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		sum = 0;
		cin >> N;
		for (int i = 1; i <= N; ++i) {
			cin >> tree[i];
			tree_sort(i);
		}
		for (int i = 1; i <= N; ++i) {
			cout << tree[i] << " ";
		}
		N /= 2;
		while (N >= 1){
			sum += tree[N];
			N /= 2;
		}
		cout << "#" << t << " " << sum << "\n";
	}
	
}