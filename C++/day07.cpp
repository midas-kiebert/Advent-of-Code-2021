#include <algorithm>
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

int median(const vector<int>& vec) {
    vector<int> v = vec;
    int middle = v.size() / 2;
    nth_element(v.begin(), v.begin() + middle, v.end());
    return v[middle];
}

int mean(const vector<int>& v) {
    int sum = 0;
    for (int i : v) { sum += i; }
    return sum / v.size();
}

// 331067
// ~0.07 ms
int part1(const INPUT_TYPE& input) {
    int m = median(input);
    int result = 0;
    for (int i : input) { result += abs(i - m); }

    return result;
}

// 92881128
// ~0.03 ms
int part2(const INPUT_TYPE& input) {
    int m = mean(input);
    int result = 0, result2 = 0;
    for (int i : input) {
        int n = abs(i - m);
        result += (n * n + n) / 2;
        n = abs(i - (m + 1));
        result2 += (n * n + n) / 2;
    }

    return min(result, result2);
}

int main() {
    auto input = getInput("../inputs/day07.txt");

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