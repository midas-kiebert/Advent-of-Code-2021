#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <sstream>
#include <iomanip>

using namespace std;

#define INPUT_TYPE vector<int>

struct line {
    int x1, y1, x2, y2;
};

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string temp;
    string coord1Stream, coord2Stream;
    vector<line> lines;

    while (getline(inputFile, temp)) {
        istringstream ss(temp);
        ss >> coord1Stream;
        ss.ignore(4);
        ss >> coord2Stream;

        line new_line;
    }

    cout << coord1Stream << " " << coord2Stream << '\n';
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

    auto start2 = chrono::high_resolution_clock::now();
    auto ans2 = part2(input);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed2 = (end2 - start2) * 1000;

    int w = max(to_string(ans1).length(), to_string(ans2).length());
    cout << left << setw(20) << ans1 << "Solved in " << elapsed.count() << " ms\n";
    cout << left << setw(20) << ans2 << "Solved in " << elapsed2.count() << " ms\n";
}