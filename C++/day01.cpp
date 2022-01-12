#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

clock_t start, stop;
float time_taken;

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

int main() {
    vector<int> input = getInput("../inputs/day01.txt");

    start = clock();
    int part1 = 0;
    for (int i = 1; i < input.size(); i++) {
        if (input[i] > input[i - 1]) {
            part1++;
        }
    }
    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part1 << "\t\tSolved in " << time_taken << " ms\n";

    start = clock();
    int part2 = 0;
    for (int i = 3; i < input.size(); i++) {
        if (input[i] > input[i - 3]) {
            part2++;
        }
    }

    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part2 << "\t\tSolved in " << time_taken << " ms\n";
}