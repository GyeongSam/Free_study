#include <iostream>
int T,t,ans;
char card[8];
char p[8];
bool choice[8];

bool is_bg(int d) {
	return ((p[d] == p[d + 1] && p[d + 1] == p[d + 2]) or (p[d] + 1 == p[d + 1] && p[d + 1] + 1 == p[d + 2]));
}

void bk(int n) {
	if (ans) return;
	if (n==6) {
		if (is_bg(0) && is_bg(3)) {
			ans = 1;
		}
	}
	else {
		for (int i = 0; i < 6; ++i) {
			if (!choice[i]) {
				p[n] = card[i];
				choice[i] = 1;
				bk(n + 1);
				choice[i] = 0;
				p[n] = '0';
			}
		}
	}
}

int main() {
	scanf("%d", &T);
	std::cin.ignore();
	while (++t <= T) {
		ans = 0;
		scanf("%s", card);
		bk(0);
		if (ans) printf("#%d Baby Gin\n",t);
		else printf("#%d Lose\n", t);
	}
}