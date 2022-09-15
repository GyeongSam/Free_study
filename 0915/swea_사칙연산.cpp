
#include <iostream>

using namespace std;

char sub[10];
int nd_num, N, nd_L, nd_R;

float value[1001] = { 0, };
int L_son[1001];
int R_son[1001];

float in_order(int i) {
	if (value[i]>0) {
		return value[i];
	}
	if (value[i] == -1) {
		return in_order(L_son[i]) + in_order(R_son[i]);
	}
	else if (value[i] == -2) {
		return in_order(L_son[i]) - in_order(R_son[i]);
	}
	else if (value[i] == -3) {
		return in_order(L_son[i]) * in_order(R_son[i]);
	}
	else if (value[i] == -4) {
		return in_order(L_son[i]) / in_order(R_son[i]);
	}
	return 0;
}


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	for (int T = 1; T < 11; ++T) {
		cin >> N;
		while (N--) {
			cin >> nd_num >> sub;
			if (sub[0] >= '0' && sub[0] <= '9') {
				value[nd_num] = atof(sub);
			}
			else {
				cin >> nd_L >> nd_R;
				if (sub[0] == '+') value[nd_num] = -1;
				else if (sub[0] == '-') value[nd_num] = -2;
				else if (sub[0] == '*') value[nd_num] = -3;
				else if (sub[0] == '/') value[nd_num] = -4;
				L_son[nd_num] = nd_L;
				R_son[nd_num] = nd_R;
			}

		}
		cout << "#"<<T<<" "<<in_order(1)<<"\n";
	}

}