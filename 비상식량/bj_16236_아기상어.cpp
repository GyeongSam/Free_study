#include <iostream>
using namespace std;
struct IJ {
	int I;
	int J;
};
int sea[20][20] = { 0, };
int N, cnt = 0, sz = 2,time=0;

IJ find_fish(IJ ij) {
	int D=0;
	while (D++<2*N) {
		for (int di = -D; di <= D; di++) {
			int dj = D - abs(di);
			int dI = ij.I + di;
			int dJ1 = ij.J - dj;
			int dJ2 = ij.J + dj;
			if (0 <= dI && dI < N && 0 <= dJ1 && dJ1 < N && sea[dI][dJ1] && sea[dI][dJ1] <= sz) {
				ij.I = dI; ij.J = dJ1; return ij;
			}
			if (0 <= dI && dI < N && 0 <= dJ2 && dJ2 < N && sea[dI][dJ2] && sea[dI][dJ2] <= sz) {
				ij.I = dI; ij.J = dJ2; return ij;
			}
		}
	}
	ij.I = -1;
	return ij;
}


int main() {
	IJ location,next_location;
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> sea[i][j];
			if (sea[i][j] == 9) { location.I = i; location.J = j; }
		}
	}
	while (1) {
		next_location = find_fish(location);
		if (next_location.I == -1) { break; }
		time += abs(location.I - next_location.I) + abs(location.J - next_location.J);
		location = next_location;
		sea[location.I][location.J] = 0;
		if (++cnt == sz) {
			sz++;
			cnt = 0;
		}
	}

	cout << time << "\n";


}