#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <sstream>

using namespace std;

clock_t start, stop;
float time_taken;

vector<pair<string, int>> getInput(string path) {
    vector<pair<string, int>> input;
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

int main() {
    vector<pair<string, int>> input = getInput("../inputs/day02.txt");
    start = clock();

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
    part1 = horizontal * depth;

    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part1 << "\t\tSolved in " << time_taken << " ms\n";

    start = clock();
    int horizontal2 = 0, depth2 = 0, aim = 0, part2;
    for (auto line : input) {
        if (line.first == "forward") {
            horizontal2 += line.second;
            depth2 += aim * line.second;
        } else if (line.first == "up") {
            aim -= line.second;
        } else {
            aim += line.second;
        }
    }
    part2 = horizontal2 * depth2;

    stop = clock();
    time_taken = (float) (stop - start) / CLOCKS_PER_SEC * 1000;

    cout << part2 << "\tSolved in " << time_taken << " ms\n";
}