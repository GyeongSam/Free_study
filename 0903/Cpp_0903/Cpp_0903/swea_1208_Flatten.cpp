#include <iostream>

int main() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);
	int t = 0,sub;
	while (t++ < 10) {
		int N;
		std::cin >> N;
		int cnt_arr[101]{};					//0���� �ʱ�ȭ �� ī��Ʈ �迭�Դϴ�.
		for (int i = 1; i <= 100; i++) {
			std::cin >> sub;
			cnt_arr[sub] +=1;				//��ǲ�� ������ �ε�����ŭ�� ���̰� ��ִ��� üũ�մϴ�.
		}
		sub = 0;
		for (int j = 100; j >= 1; j--) {	//�Ųٷ� ���� �ش� ���̿� �� ���� ��ִ��� üũ�մϴ�.
			sub += cnt_arr[j];
			cnt_arr[j] = sub;
		}

		int B = 0, B_sum=0, T = 100, T_sum=0;	//T�� ž���� �������� , B�� ���ҿ��� ž���� �ö󰩴ϴ�.
		
		while (B_sum <= N) { B_sum += 100 - cnt_arr[B++]; }	//���ҿ��� ä�����ϴ�.
		while (T_sum <= N) { T_sum += cnt_arr[T--]; }		//ž���� ������ϴ�.
		std::cout <<"#"<<t<<" "<< T - B << "\n";

	}
}