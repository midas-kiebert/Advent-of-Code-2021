#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

vector<int> getInput(string path) {
    vector<int> input;
    ifstream inputFile;
    inputFile.open(path);
    string line;
    while (getline(inputFile, line)) {
        input.push_back(stoi(line));
    }
    inputFile.close();
    return input;
}

// 1390
// ~0.01 ms
int part1(const vector<int>& input) {
    int result = 0;
    int size = input.size();
    for (int i = 1; i < size; i++) {
        result += input[i] > input[i - 1];
    }
    return result;
}

// 1457
// ~0.01 ms
int part2(const vector<int>& input) {
    int result = 0;
    int size = input.size();
    for (int i = 3; i < size; i++) {
        result += input[i] > input[i - 3];
    }
    return result;
}

int main() {
    auto input = getInput("../inputs/day01.txt");

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