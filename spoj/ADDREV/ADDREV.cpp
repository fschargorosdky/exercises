// http://www.spoj.com/problems/ADDREV/
#include <iostream>
#include <math.h>
using namespace std;

int digitsCount(int x){
	int res = 1;    
	while(x / 10 > 0){
		x/= 10;
		res++;
	}
	return res;
}

int main()
{
	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		int x;
		int y;
		cin >> x;
		cin >> y;  	
		if(y > x){
			int aux = y;
			y = x;
			x = aux;
		}
		int res = 0;
		int dx = digitsCount(x);
		int dy = digitsCount(y);  	
		int carry = 0;
		while(dy > 0){
			int ydigit = y / pow(10, dy - 1);
			int xdigit = x / pow(10, dx - 1);
			
			y %= int(pow(10, dy - 1));
			x %= int(pow(10, dx - 1));
			int sum = xdigit + ydigit + carry;
			carry = sum >= 10?1:0;
			sum %= 10;
			res += sum * pow(10, dx - 1);
			dx--;
			dy--;
		}
		while(dx > 0){
			int xdigit = x / pow(10, dx - 1);
			x %= int(pow(10, dx - 1));
			int sum = xdigit + carry;
			carry = sum >= 10?1:0;
			sum %= 10;
			res += sum * pow(10, dx - 1);
			dx--;	
		}
		if(carry){
			res = res * 10 + carry;	
		}		
		cout << res << endl;
	}
}