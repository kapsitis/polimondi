#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " input.txt output.txt\n";
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cerr << "Error: Could not open input file '" << argv[1] << "'\n";
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(inputFile, line)) {
        lines.push_back(line);
    }
    inputFile.close();

    std::sort(lines.begin(), lines.end());

    std::ofstream outputFile(argv[2]);
    if (!outputFile) {
        std::cerr << "Error: Could not open output file '" << argv[2] << "'\n";
        return 1;
    }

    for (const auto &sortedLine : lines) {
        outputFile << sortedLine << '\n';
    }
    outputFile.close();

    return 0;
}
