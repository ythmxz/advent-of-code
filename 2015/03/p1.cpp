// Day 3: Perfectly Spherical Houses in a Vacuum (Part 1) https://adventofcode.com/2015/day/3
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    string input = "";
    cin >> input;

    int x = 0;
    int y = 0;

    vector<pair<int, int>> positions(1, make_pair(x, y));

    int houses = 1;
    bool visited = false;

    for (int i = 0; i < input.length(); i++) {
        switch (input[i]) {
        case '<':
            x--;
            break;
        case '>':
            x++;
            break;
        case '^':
            y++;
            break;
        case 'v':
            y--;
            break;
        }

        pair<int, int> currentPos(x, y);

        for (int i = 0; i < positions.size(); i++) {
            if (currentPos == positions[i]) {
                visited = true;
                break;
            }
        }

        if (!visited) {
            positions.push_back(currentPos);
            houses++;
        }

        visited = false;
    }

    cout << houses << endl;

    return 0;
}
