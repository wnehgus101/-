#include <iostream>

using namespace std;

int main() {
    int h, m; //h는 입력받는 시간이며 m은 입력받는 분을 의미한다.

    cin >> h >> m;

    if ( m < 45 ) { //m의 값에 따라서 h가 변하는 경우
        if ( h == 0 ) { //그 중 h의 값이 0인 경우
            cout << 23 << " " << m+15 << endl;
        }
        else { // h가 0이 아닌 경우
            cout << h-1 << " " << m+15 << endl;
        }
    }

    else { // h의 값이 변하지 않는 경우
        cout << h << " " << m-45 << endl;
    }
}
