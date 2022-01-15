#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define INPUT_TYPE vector<Line>

const int GRID_SIZE = 1000;

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

int sign(int x) {
    return (x > 0) - (x < 0);
}

bool is_between(int a, int b, int c) {
    if (c >= a && a >= b) return true;
    if (b >= a && a >= c) return true;
    return false;
}

// 8350
// ~2.2 ms
int part1(const INPUT_TYPE& input) {
    int overlaps = 0;
    int grid[GRID_SIZE][GRID_SIZE] = {0};

    for (auto l : input) {
        int dx = sign(l.p2.x - l.p1.x);
        int dy = sign(l.p2.y - l.p1.y);

        while(dx * dy == 0) {
            if (grid[l.p1.y][l.p1.x]++ == 1) overlaps++;
            if (l.p1.x == l.p2.x && l.p1.y == l.p2.y) break;

            l.p1.x += dx;
            l.p1.y += dy;
        }
    }
    return overlaps;
}

// 19374
// ~1.4 ms
int part2(const INPUT_TYPE& input) {
    int overlaps = 0;
    int grid[GRID_SIZE][GRID_SIZE] = {0};

    for (auto l : input) {
        int dx = sign(l.p2.x - l.p1.x);
        int dy = sign(l.p2.y - l.p1.y);

        while(true) {
            if (grid[l.p1.y][l.p1.x]++ == 1) overlaps++;
            if (l.p1.x == l.p2.x && l.p1.y == l.p2.y) break;

            l.p1.x += dx;
            l.p1.y += dy;
        }
    }
    return overlaps;
}

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