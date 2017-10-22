#include<iostream>
#include<vector>

using namespace std;

const int SIZE = 10;

bool validateBrackets(string);

int main(){

	cout << "Hello Vectors"<<endl;

	vector<char> vec;

	string input;
	cout<<"Enter the pattern to valodate:";
	getline(cin, input);
	cout<<"You entered : "<<input<<endl;

	if(validateBrackets(input)){
		cout<<"Valid Pattern"<<endl;
	}
	else{
		cout<<"Invalid Pattern"<<endl;	
	}
	return 0;
}

void displayStack(std::vector<char> &v){
	cout<<"\nStack: ";
	for(int i=0;i<v.size();i++){
		cout << v[i] <<" ";
	}
}

bool validateBrackets(string input){
	cout << "Size of input: "<<input.size()<<endl;
	vector<char> stack;
	for(int i = 0;i<input.size();i++){
		
		char currentChar = input[i];
		
		if((currentChar == '{') || (currentChar == '[') || (currentChar == '(')){
			stack.push_back(currentChar);
		}
		else{
			if(stack.empty()){
				return false;
			}
			else{
				
				char stackTop = stack.back();
				
				if(currentChar=='}' && stackTop != '{'){
					return false;
				}
				if(currentChar==']' && stackTop != '['){
					return false;
				}
				if(currentChar==')' && stackTop != '('){
					return false;
				}
				
				stack.pop_back();

			}
		}
	}
	
	if(stack.empty()){
		return true;
	}
	else{
		return false;
	}
}