#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;

#define INPUT_TYPE vector<Line>

struct Point {
    int x, y;
};

struct Line {
    Point p1, p2;
};

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string temp;
    while (getline(inputFile, temp)) {
        istringstream ss(temp);
        string x1Str, y1Str, x2Str, y2Str;

        getline(ss, x1Str, ',');
        ss >> y1Str;
        ss.ignore(3);
        getline(ss, x2Str, ',');
        ss >> y2Str;

        Line line;
        line.p1.x = stoi(x1Str);
        line.p1.y = stoi(y1Str);
        line.p2.x = stoi(x2Str);
        line.p2.y = stoi(y2Str);

        input.push_back(line);
    }

    inputFile.close();
    return input;
}

bool is_between(int a, int b, int c) {
    if (c >= a && a >= b) return true;
    if (b >= a && a >= c) return true;
    return false;
}

int part1(const INPUT_TYPE& input) {
    int pointsWithOverlap = 0;

    for (const auto& l1 : input) {
        for (const auto& l2 : input) {
            if (l1.p1.x == l1.p2.x && l2.p1.y == l2.p2.y &&
                is_between(l1.p1.x, l2.p1.x, l2.p2.x) &&
                is_between(l2.p1.y, l1.p1.y, l1.p2.y)) {
                pointsWithOverlap++;
                cout << l1.p1.x << "," << l1.p1.y << " -> " << l1.p2.x << "," << l1.p2.y << " & " << l2.p1.x << "," << l2.p1.y << " -> " << l2.p2.x << "," << l2.p2.y << endl;
            }
        }
    }
    return pointsWithOverlap;
}

int part2(const INPUT_TYPE& input) { return 0; }

int main() {
    auto input = getInput("../inputs/day05.txt");

    auto start1 = chrono::high_resolution_clock::now();
    auto ans1 = part1(input);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = (end1 - start1) * 1000;

    cout << left << setw(20) << ans1 << "Solved in " << elapsed.count()
         << " ms\n";

    auto start2 = chrono::high_resolution_clock::now();
    auto ans2 = part2(input);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed2 = (end2 - start2) * 1000;

    cout << left << setw(20) << ans2 << "Solved in " << elapsed2.count()
         << " ms\n";
}