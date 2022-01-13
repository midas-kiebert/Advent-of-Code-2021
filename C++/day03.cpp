#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;

#define INPUT_TYPE vector<string>

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string line;
    while (getline(inputFile, line)) {
        input.push_back(line);
    }
    inputFile.close();
    return input;
}

// 4006064
// ~0.4 ms
int part1(const INPUT_TYPE& input) {
    int gamma = 0, epsilon = 0;
    for (int i = 0; i < input[0].length(); i++) {
        int ones = 0;
        for (string j : input) {
            ones += j[i] - '0';
        }
        if (ones * 2 >= input.size()) {
            gamma += 1 << input[0].length() - i - 1;
        } else {
            epsilon += 1 << input[0].length() - i - 1;
        }
    }
    return gamma * epsilon;
}

// 5941884
// ~0.7 ms
int part2(const INPUT_TYPE& input) {
    int O2, CO2;
    vector<string> numbersO2 = input, numbersCO2 = input;

    for (int i = 0; i < input[0].length(); i++) {
        int onesO2 = 0;
        for (string j : numbersO2) {
            onesO2 += j[i] - '0';
        }
        vector<string> newO2;
        for (string j : numbersO2) {
            if ((onesO2 * 2 >= numbersO2.size()) == j[i] - '0') {
                newO2.push_back(j);
            }
        }

        if (newO2.size() == 1) {
            O2 = stoi(newO2[0], 0, 2);
            break;
        }

        numbersO2 = newO2;
    }

    for (int i = 0; i < input[0].length(); i++) {
        int onesCO2 = 0;
        for (string j : numbersCO2) {
            onesCO2 += j[i] - '0';
        }
        vector<string> newCO2;
        for (string j : numbersCO2) {
            if ((onesCO2 * 2 < numbersCO2.size()) == j[i] - '0') {
                newCO2.push_back(j);
            }
        }

        if (newCO2.size() == 1) {
            CO2 = stoi(newCO2[0], 0, 2);
            break;
        }

        numbersCO2 = newCO2;
    }
    return O2 * CO2;
}

int main() {
    auto input = getInput("../inputs/day03.txt");

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
    cout << left << setw(20) << ans2 << "Solved in " << elapsed2.count() << " ms\n";}