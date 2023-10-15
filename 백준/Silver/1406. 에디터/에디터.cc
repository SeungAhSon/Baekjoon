#include <iostream>
#include <list>
#include <string>
using namespace std;
int main(void){
  string initial_str;
  int M;
  
	cin >> initial_str;
	cin >> M;
	
	
  
  list<char> editor;
  for (char c : initial_str) {
    editor.push_back(c);
  }
  auto cur = editor.end(); 
	
	while (M--){
		char input_str;
		cin >> input_str;
		
		if (input_str == 'L'&& cur != editor.begin()){
		  cur--;
		} else if (input_str == 'D'&& cur != editor.end()){
		  cur++;
		} else if (input_str == 'B'&& cur != editor.begin()){
		  cur--;
			cur = editor.erase(cur);
		}  else if (input_str == 'P'){
		  char new_char;
		  cin >> new_char;
		  editor.insert(cur, new_char);
		}
	}

	for (char c : editor) {
    cout << c;
  }
	return 0;
}