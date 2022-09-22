
#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int m = 0,I=0;
	for (int i=1; i < 10; i++){
		int n;
		cin >> n;
		if (n > m) {
			m = n;
			I = i;
		}
	}
	cout << m << '\n' << I <<'\n';
}
