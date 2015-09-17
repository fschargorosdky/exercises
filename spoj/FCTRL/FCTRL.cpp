// http://www.spoj.com/problems/ADDREV/
#include <iostream>
#include <math.h>
using namespace std;

int version1(long N){
	long res = 0;
	int power = log10(N) / log10(5);
	int factor = 5;
	cout << power << endl;
	for(long j = 1; j <= power; j++){			
		res += N / factor;
		cout << res << endl;
		factor *= 5;
	}	
	return res;
}

int version2(long N){
	long res = 0;
	int factor = 5;
	while(factor <= N){			
		res += N / factor;
		factor *= 5;
	}	
	return res;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		long N;
		long res = 0;
		cin >> N;
		int x = version1(N);
		cout << "N: " << N << ", res: " << x << endl;
	}
}