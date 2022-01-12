#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;

#define INPUT_TYPE vector<int>

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string line;
    while (getline(inputFile, line)) {

    }
    inputFile.close();
    return input;
}

int part1(const INPUT_TYPE& input) {

}

int part2(const INPUT_TYPE& input) {

}

int main() {
    auto input = getInput("../inputs/dayXX.txt");

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