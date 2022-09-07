#include <iostream>
#include <vector>

int N, cnt = 0;
std::vector<int> queen;
bool can=1;

void BT(int i) {
	if (i == N) {
		cnt++;
		return;
	}
	else {
		for (int j = 0; j < N; j++) {
			int l = j, r = j;
			for (int k = queen.size()-1; k >=0; k--) {
				if (queen[k] == j || --l == queen[k] || ++r == queen[k]) { can = 0; break; }
			}
			if (can == 0) { can = 1; continue; }
			queen.push_back(j);
			BT(i + 1);
			queen.pop_back();
		}
	}
	return;
}

int main() {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cin >> N;
		BT(0);
		std::cout << "#" << t <<" " << cnt << "\n";
		cnt = 0;
	}
	return 0;
}


/*std::cout << "\n이번 queen 배치는\n";
for (int k = 0; k < queen.size(); k++) {
	std::cout << queen[k] << " ";
}
std::cout << "\n 추가할지 말지 결정할 j는 " << j << "\n";*/