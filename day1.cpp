#include <iostream> 
#include <vector>
#include <fstream>
#include <string> 
#include <queue>
using namespace std;

int main() {
    // cout << "hello world!" << endl;

    vector<int> s(10, 0);

    ifstream file("input_1.txt");
    std::string mystring;
    int number = 0;
    int max_number = 0;

    priority_queue<int> pq;


    if (file.is_open()) {

        while (file) {
            getline(file, mystring);
            
            
            if (mystring.empty()) {
                max_number = max(max_number, number);
                pq.push(-1 * number);
                if (pq.size() > 3) {
                    pq.pop();
                }
                number = 0;
            } 

            else {
                number += stoi(mystring);
            }
            // cout << mystring << ": " << file.tellg() << "\n";
        }  
    }

    int total = 0;
    for (int i = 0; i < 3; ++i) {
        total += -1*pq.top();
        pq.pop();

    }

    cout << total << endl;

    // cout << mystring << endl;

    return 0;
}