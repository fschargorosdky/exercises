// https://projecteuler.net/problem=1
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int res = 0;
	int i = 3;
	while(i < 1000){
		res += i;
		i += 3;
	}
	i = 5;
	while(i < 1000){
		if(i % 3 != 0){
			res += i;
		}
		i += 5;
	}	
	cout << res << endl;
}