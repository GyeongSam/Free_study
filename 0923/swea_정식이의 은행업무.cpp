#include <iostream>

int len(char a[]) {
	int i = -1;
	while (*(a + (++i)) != '\0');
	return i;
}


int to10(char a[],int n,int l) {
	int c = 1,sum=0;
	for (int j = l - 1; j >= 0; --j) {
		sum += (*(a + j) - '0')*c;
		c *= n;
	}
	return sum;
}

char C[3] = { '0','1','2' };

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int ans = 0;
		char i2[41];
		char i3[41];
		scanf("%s", i2);
		scanf("%s", i3);

		int len_i2 = len(i2);
		int len_i3 = len(i3);

		int I2 = to10(i2, 2,len_i2);

		for (int i = 0; i<len_i3; ++i) {
			char sub = i3[i];
			for (int d = 0; d < 3; ++d) {
				if (sub == C[d]) continue;
				else (i3[i] = C[d]);
				int I3 = to10(i3, 3, len_i3);
				for (int j = 0; j < len_i2; ++j) {
					//printf("i2:%d, i3:%d\n", (I2 ^ (1 << j)), I3);
					if ((I2 ^ (1 << j)) == I3) {
						ans = I3;
						break;
					}
				
				}
				if (ans) break;
			}
			i3[i] = sub;
			if (ans) break;
		}
		printf("#%d %d\n",t, ans);
		
	}

}