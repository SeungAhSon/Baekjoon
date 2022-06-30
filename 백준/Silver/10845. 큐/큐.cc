#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;
queue <int> q;

int main() {
	int N; cin>>N;
	while(N--){
		string cmd; cin>>cmd;
		if(cmd =="push"){
			int inp; cin>>inp;
			q.push(inp);
		}
		if(cmd=="pop"){
			if(q.empty()){
				cout<<"-1\n";
			}
			else{
				cout<<q.front()<<"\n";
				q.pop();
			}			
		}
		if(cmd=="size"){
			cout<<q.size()<<"\n";
		}
		if(cmd=="empty"){
			if(q.empty()){
				cout<<"1\n";
			}
			else{
				cout<<"0\n";
			}			
		}

		if(cmd=="front"){
			if(q.empty()){
				cout<<"-1\n";
			}
			else{
				cout<<q.front()<<"\n";
			}
		}
		if(cmd=="back"){
			if(q.empty()){
				cout<<"-1\n";
			}
			else{
				cout<<q.back()<<"\n";
			}
		}
	}
	return 0;
}