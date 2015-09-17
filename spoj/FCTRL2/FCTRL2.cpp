// http://www.spoj.com/problems/FCTRL2/
#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;
	vector<unsigned long long> factorials(101, 0);
	factorials[1] = 1;
	int biggestFactorial = 1;
	for(int i = 0; i < T; i++){
		int N;
		cin >> N;
		for(int j = biggestFactorial + 1; j <= N; j++){
			factorials[j] = j * factorials[j - 1];
		}
		biggestFactorial = N;
		cout << factorials[N] << endl;
	}
}