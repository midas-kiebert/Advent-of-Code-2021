#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

#define INPUT_TYPE pair<vector<int>, vector<BingoBoard>>

const int BOARD_SIZE = 5;

struct BingoNumber {
    int num;
    bool marked;
};

struct BingoBoard {
    vector<BingoNumber> nums;
    bool done;

    void mark(int n) {
        for (BingoNumber& bn : nums) {
            if (n == bn.num) {
                bn.marked = true;
                break;
            }
        }
    }

    bool is_done() {
        // Check Columns
        for (int i = 0; i < BOARD_SIZE; i++) {
            bool col_done = true;
            for (int j = 0; col_done && j < BOARD_SIZE * BOARD_SIZE;
                 j += BOARD_SIZE) {
                col_done = col_done && nums[i + j].marked;
            }
            if (col_done) {
                done = true;
                return true;
            }
        }

        // Check Rows
        for (int i = 0; i < BOARD_SIZE * BOARD_SIZE; i += BOARD_SIZE) {
            bool row_done = true;
            for (int j = 0; row_done && j < BOARD_SIZE; j++) {
                row_done = row_done && nums[i + j].marked;
            }
            if (row_done) {
                done = true;
                return true;
            }
        }

        return false;
    }

    int unmarked_sum() {
        int sum = 0;
        for (BingoNumber bn : nums) {
            if (!bn.marked) {
                sum += bn.num;
            }
        }
        return sum;
    }
};

vector<int> split(const string& s, char delimiter) {
    vector<int> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(stoi(token));
    }
    return tokens;
}

INPUT_TYPE getInput(string path) {
    INPUT_TYPE input;
    ifstream inputFile;
    inputFile.open(path);
    string line;
    vector<string> lines;

    while (getline(inputFile, line)) {
        lines.push_back(line);
    }

    input.first = split(lines[0], ',');

    for (int i = 2; i < lines.size(); i += BOARD_SIZE + 1) {
        BingoBoard bb;
        bb.done = false;
        BingoNumber bn;

        for (int j = 0; j < BOARD_SIZE; j++) {
            stringstream ss(lines[i + j]);
            string s;
            while (ss >> s) {
                bn.num = stoi(s);
                bn.marked = false;
                bb.nums.push_back(bn);
            }
        }
        input.second.push_back(bb);
    }

    inputFile.close();
    return input;
}

// 41668
// ~0.6 ms
int part1(const INPUT_TYPE& input) {
    vector<BingoBoard> boards = input.second;
    for (int n : input.first) {
        for (BingoBoard& bb : boards) {
            bb.mark(n);
            if (bb.is_done()) {
                return bb.unmarked_sum() * n;
            }
        }
    }
    return 0;
}

// 10478
// ~2.6 ms
int part2(const INPUT_TYPE& input) {
    vector<BingoBoard> boards = input.second;
    int boards_left = boards.size();

    for (int n : input.first) {
        for (BingoBoard& bb : boards) {
            if (bb.done)
                continue;
            bb.mark(n);
            if (bb.is_done() && --boards_left == 0) {
                return bb.unmarked_sum() * n;
            }
        }
    }
    return 0;
}

int main() {
    auto input = getInput("../inputs/day04.txt");

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