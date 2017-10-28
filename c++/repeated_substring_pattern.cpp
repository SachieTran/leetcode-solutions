#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>

using namespace std;


int main(){
    map<char, int>m;
    string input = "abaababaab";
    for(int i=0;i<input.size();i++){
        char currentChar = input[i];
        if(m.find(currentChar)!=m.end()){
            m.find(currentChar)->second+=1;
        }
        else{
            m.insert(make_pair(currentChar, 1));
        }
    }
    for(map<char,int>::iterator it = m.begin();it!=m.end();++it){
        cout<<it->first<<" "<<it->second<<endl;
    }
    set<int> count;
    count.insert(m.begin()->second);
    for(map<char,int>::iterator it = next(m.begin(),1);it!=m.end();++it){
        if(count.find(it->second)==count.end()){
            return false;
        }
    }
    return 0;
}