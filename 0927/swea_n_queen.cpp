#include <iostream>
#include <vector>

int N, cnt = 0;
std::vector<int> queen;
bool can = 1;

void BT(int i) {    //i�� ��� �����Դϴ�.
	if (i == N) {    //i�� ���� ������ ���ٸ� ī��Ʈ���ϳ� ���ݴϴ�.
		cnt++;
		return;
	}
	else {
		for (int j = 0; j < N; j++) {
			int l = j, r = j;
			for (int k = queen.size() - 1; k >= 0; k--) {
				if (queen[k] == j || --l == queen[k] || ++r == queen[k]) { can = 0; break; }
			}    //���� ���� �߰��� queen �迭�� ���� ���� �� �ִ� n���� Ȯ���մϴ�.
			if (can == 0) { can = 1; continue; }    //���� �� ���ٸ� �������� �Ѿ�ϴ�.
			queen.push_back(j); //���� �� �ִٸ� j�� �߰��ϰ�
			BT(i + 1);            //�� Ž���մϴ�.
			queen.pop_back();    //Ž���� �����ؼ� ���ƿԴٸ� �߰��ߴ� �� ���� �մϴ�.
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