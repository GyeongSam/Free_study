#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int T, tc,N,M,s;
string IP;
int btoi[10] = { 0b0001101,0b0011001,0b0010011,0b0111101,0b0100011,0b0110001,0b0101111,0b0111011,0b0110111,0b0001011};
vector <int> secret;


bool is_valid() {
	return !((3 * (secret[0] + secret[2] + secret[4] + secret[6]) + secret[1] + secret[3] + secret[5] + secret[7]) % 10);
}


int StoI(string A) {
	int sum=0;
	for (int x = 0; x < 7; ++x) {
		sum+=(A[x]-'0') * (pow(2, 6 - x));
	}
	for (int i = 0; i < 10; ++i) {
		if (btoi[i] == sum) {
			return i;
		}
	}
	return -1;
}



int main() {
	scanf("%d", &T);
	while (++tc <= T) {
		secret.clear();

		scanf("%d %d", &N, &M);
		cin.ignore();
		while (N--) {
			getline(cin, IP);

			if (!secret.empty()) continue;

			for (s = IP.size() - 1; s >= 55; --s) {
				if (IP[s] == '1') {
					for (int x = s - 55; x <= s; x+=7) {
						secret.push_back(StoI(IP.substr(x, 7)));
					}
					break;
				}
			}
		}

		if (is_valid()) {
			int sum = 0;
			for (int i = 0; i < 8; ++i) {
				sum += secret[i];
			}
			printf("#%d %d\n", tc, sum);
		}
		else printf("#%d -1\n", tc);
	}
	
}