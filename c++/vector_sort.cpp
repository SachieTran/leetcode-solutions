#include<iostream>
#include<vector>

using namespace std;

const int SIZE = 10;

int main(){
	vector<int> v;
	int input;
	for(int i=0;i<SIZE;i++){
		cin >> input;
		v.push_back(input);
	}
	sort(v.rbegin(),v.rend());
	for(int i=0;i<SIZE;i++){
		cout << v[i];
	}
	return 0;
}