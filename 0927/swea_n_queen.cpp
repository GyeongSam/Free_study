#include <iostream>
#include <vector>

int N, cnt = 0;
std::vector<int> queen;
bool can = 1;

void BT(int i) {    //i는 재귀 깊이입니다.
	if (i == N) {    //i가 깊이 끝까지 갔다면 카운트를하나 해줍니다.
		cnt++;
		return;
	}
	else {
		for (int j = 0; j < N; j++) {
			int l = j, r = j;
			for (int k = queen.size() - 1; k >= 0; k--) {
				if (queen[k] == j || --l == queen[k] || ++r == queen[k]) { can = 0; break; }
			}    //지금 까지 추가된 queen 배열을 통해 놓을 수 있는 n인지 확인합니다.
			if (can == 0) { can = 1; continue; }    //놓을 수 없다면 다음으로 넘어갑니다.
			queen.push_back(j); //놓을 수 있다면 j를 추가하고
			BT(i + 1);            //더 탐색합니다.
			queen.pop_back();    //탐색에 실패해서 돌아왔다면 추가했던 걸 제거 합니다.
		}
	}
	return;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &N);
		cnt = 0; queen.clear();
		BT(0);
		printf("#%d %d\n",t, cnt);
	}

	
;
}