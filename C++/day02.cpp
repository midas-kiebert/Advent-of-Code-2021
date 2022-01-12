#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <sstream>
#include <chrono>
#include <iomanip>

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
    std::chrono::duration<double> elapsed = (end1 - start1) * 1000;

    auto start2 = chrono::high_resolution_clock::now();
    auto ans2 = part2(input);
    auto end2 = chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed2 = (end2 - start2) * 1000;

    int w = max(to_string(ans1).length(), to_string(ans2).length());
    cout << setw(w) << ans1 << setw(20) << "Solved in " << elapsed.count() << " ms\n";
    cout << setw(w) << ans2 << setw(20) << "Solved in " << elapsed2.count() << " ms\n";
}