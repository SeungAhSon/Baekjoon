#include <iostream>
using namespace std;

int main() 
{
    int K;
    cin >> K;
    while (K--) {
      int P,M;
      cin >> P >> M;
      
      bool arr[P+1] = {};
      int count = 0;
      for(int j=0; j<P; ++j){
        int temp;
        cin>> temp;
        if (arr[temp]) count++;
        else arr[temp]=1;
      }
      cout << count << endl;
    }
    
    return 0;
}