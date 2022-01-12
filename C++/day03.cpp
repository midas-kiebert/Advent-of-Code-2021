#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;

clock_t start, stop;
float time_taken;

vector<string> getInput(string path) {
    vector<string> input;
    ifstream inputFile;
    inputFile.open(path);
    string str;
    while (getline(inputFile, str)) {
        input.push_back(str);
    }
    inputFile.close();
    return input;
}

int main() {
    vector<string> input = getInput("../inputs/day03.txt");
    start = clock();

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
    int part1 = gamma * epsilon;

    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part1 << "\t\tSolved in " << time_taken << " ms\n";

    start = clock();

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
    int part2 = O2 * CO2;

    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part2 << "\t\tSolved in " << time_taken << " ms\n";
}