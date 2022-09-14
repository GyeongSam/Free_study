#include <iostream>
#include <vector>

int N,cnt=0;
std::vector<int> queen;
bool visit[15];


void BT(int i) {
	if (i == N) {
		cnt++;
		return;
	}
	else {
		for (int j = 0; j < N; j++) {
			if (visit[j]) continue;
			visit[j] = 1;
			queen.push_back(i);
			BT(i + 1);
			queen.pop_back();
			visit[j] = 0;
		}
																																																																																																		
	}
	return;
}

int main() {
	std::cin >> N;
	BT(0);
	std::cout << cnt << "\n";
}