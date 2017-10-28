#include<iostream>
#include<list>

using namespace std;

const int SIZE = 10;

int main(){
	list<int> v;
	int input;
	for(int i=0;i<SIZE;i++){
		cin >> input;
		v.push_back(input);
	}
}