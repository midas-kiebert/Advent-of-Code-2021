#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define INPUT_TYPE vector<pair<point, point>>

struct point {
    int x, y;
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

        pair<point, point> line;
        line.first.x = stoi(x1Str);
        line.first.y = stoi(y1Str);
        line.second.x = stoi(x2Str);
        line.second.y = stoi(y2Str);

        input.push_back(line);
    }

    inputFile.close();
    return input;
}

int part1(const INPUT_TYPE& input) {
    return 0;
}

int part2(const INPUT_TYPE& input) {
    return 0;
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