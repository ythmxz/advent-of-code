// Day 1: Not Quite Lisp (Part 2) https://adventofcode.com/2015/day/1#part2
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    string input = "";
    cin >> input;

    int floor = 0;

    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '(') {
            floor++;
        } else {
            floor--;
        }

        if (floor == -1) {
            cout << i + 1 << endl;
            break;
        }
    }

    return 0;
}
