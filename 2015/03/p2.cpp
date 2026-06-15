// Day 3: Perfectly Spherical Houses in a Vacuum (Part 2) https://adventofcode.com/2015/day/3#part2
#include <bits/stdc++.h>

using namespace std;

int main(void) {
    string input = "";
    cin >> input;

    int santaX = 0;
    int santaY = 0;

    int robotX = santaX;
    int robotY = santaY;

    vector<pair<int, int>> positions(1, make_pair(santaX, santaY));

    int houses = 1;
    bool visited = false;

    for (int i = 0, j = 1; i < input.length(); i += 2, j += 2) {
        switch (input[i]) {
        case '<':
            santaX--;
            break;
        case '>':
            santaX++;
            break;
        case '^':
            santaY++;
            break;
        case 'v':
            santaY--;
            break;
        }

        switch (input[j]) {
        case '<':
            robotX--;
            break;
        case '>':
            robotX++;
            break;
        case '^':
            robotY++;
            break;
        case 'v':
            robotY--;
            break;
        }

        pair<int, int> currentSantaPos(santaX, santaY);

        for (int i = 0; i < positions.size(); i++) {
            if (currentSantaPos == positions[i]) {
                visited = true;
                break;
            }
        }

        if (!visited) {
            positions.push_back(currentSantaPos);
            houses++;
        }

        visited = false;

        pair<int, int> currentRobotPos(robotX, robotY);

        for (int i = 0; i < positions.size(); i++) {
            if (currentRobotPos == positions[i]) {
                visited = true;
                break;
            }
        }

        if (!visited) {
            positions.push_back(currentRobotPos);
            houses++;
        }

        visited = false;
    }

    cout << houses << endl;

    return 0;
}
