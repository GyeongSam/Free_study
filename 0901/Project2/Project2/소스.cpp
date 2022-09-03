#include<iostream>
using namespace std;
int T, t = 0, a = 0, i; 
char s[51]; 
int main() { 
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> T;
	while (t++ < T) {
		a = 0;
		cin >> s; 
		i = -1; 
		while (s[++i] != '\0') { 
			if (s[i] == '(') { a++; i++; } 
			else if (s[i] == ')')a++; 
		}
		cout << '#' << t << ' ' << a << '\n'; }
	return 0; 
}