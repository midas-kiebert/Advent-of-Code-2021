#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

#define INPUT_TYPE vector<int>

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string num;
    while (getline(inputFile, num, ',')) { input.push_back(stoi(num)); }
    inputFile.close();
    return input;
}

// 380243
// ~0.005 ms
int part1(const INPUT_TYPE& input) {
    int age_groups[9] = { 0 };
    int amount = 0;
    for (int i : input) {
        age_groups[i]++;
        amount++;
    }

    for (int i = 0; i < 80; i++) {
        age_groups[(i + 7) % 9] += age_groups[i % 9];
        amount += age_groups[i % 9];
    }

    return amount;
}

// 1708791884591
// ~0.006 ms
long part2(const INPUT_TYPE& input) {
    long age_groups[9] = { 0 };
    long amount = 0;
    for (int i : input) {
        age_groups[i]++;
        amount++;
    }

    for (int i = 0; i < 256; i++) {
        age_groups[(i + 7) % 9] += age_groups[i % 9];
        amount += age_groups[i % 9];
    }

    return amount;
}

int main() {
    auto input = getInput("../inputs/day06.txt");

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