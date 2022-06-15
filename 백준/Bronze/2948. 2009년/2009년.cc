#include <iostream>
using namespace std;
void check_day(int N){
    if(N%7==1) cout<<"Thursday";
    else if(N%7==2) cout<<"Friday";
    else if(N%7==3) cout<<"Saturday";
    else if(N%7==4) cout<<"Sunday";
    else if(N%7==5) cout<<"Monday";
    else if(N%7==6) cout<<"Tuesday";
    else if(N%7==0) cout<<"Wednesday";
}

int main(){
    int x,y; cin>>y>>x;
    int days = y;
    for(int i=1;i<x;i++){
        if(i==1||i==3||i==5||i==7||i==8||i==10) days+=31;
        else if(i==2) days+=28;
        else if(i==4||i==6||i==9||i==11)days+=30;
    }
    check_day(days);

    return 0;
}