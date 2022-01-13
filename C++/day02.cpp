#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;

#define INPUT_TYPE vector<pair<string, int>>

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string line;
    while (getline(inputFile, line)) {
        string temp;
        pair<string, int> p;
        stringstream ss(line);
        ss >> p.first;
        ss >> temp;
        p.second = stoi(temp);
        input.push_back(p);
    }
    inputFile.close();
    return input;
}

// 2150351
// ~0.07 ms
int part1(const INPUT_TYPE& input) {
    int horizontal = 0, depth = 0, part1;
    for (auto line : input) {
        if (line.first == "forward") {
            horizontal += line.second;
        } else if (line.first == "up") {
            depth -= line.second;
        } else {
            depth += line.second;
        }
    }
    return horizontal * depth;
}

// 1842742223
// ~0.07 ms
int part2(const INPUT_TYPE& input) {
    int horizontal = 0, depth = 0, aim = 0;
    for (auto line : input) {
        if (line.first == "forward") {
            horizontal += line.second;
            depth += aim * line.second;
        } else if (line.first == "up") {
            aim -= line.second;
        } else {
            aim += line.second;
        }
    }
    return horizontal * depth;
}

int main() {
    auto input = getInput("../inputs/day02.txt");

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