#define _CRT_SECURE_NO_WARNINGS
#include <iostream>


#include <string>
#include <vector>
#define F(x,X) for(int x=0;x<X;++x)
#define F_(x,X) for(int x=X-1;x>=0;--x)

using namespace std;

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
	bool answer = true;
	vector <vector<int>> select(4);
	int M = key.size();
	int N = lock.size();
	int cnt_key = 0;
	int cnt_lock = 0;
	int cnt;

	F(i, N) F(j, N) if (key[i][j]) cnt_key++;
	F(i, N) F(j, N) if (!lock[i][j]) cnt_lock++;

	cnt = 0;
	F(i, M) {
		F(j, M) {
			if (key[i][j]) cnt++;
		}
		if (cnt_key - cnt > cnt_lock) continue;
		if (cnt_key - cnt == cnt_lock) select[0].push_back(-i - 1);
		if (cnt_key - cnt < cnt_lock) break;
	}





	return answer;
}



int main() {
	solution({ {0, 0, 0}, {1, 0, 0}, {0, 1, 1} }, { {1, 1, 1}, {1, 1, 0}, {1, 0, 1} });
}