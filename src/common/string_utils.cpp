//
// Copyright 2015 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//
// string_utils:
//   String helper functions.
//

#include "string_utils.h"

#include <fstream>
#include <sstream>

namespace angle
{

void SplitString(const std::string &input,
                 char delimiter,
                 std::vector<std::string> *tokensOut)
{
    std::istringstream stream(input);
    std::string token;

    while (std::getline(stream, token, delimiter))
    {
        if (!token.empty())
        {
            tokensOut->push_back(token);
        }
    }
}

void SplitStringAlongWhitespace(const std::string &input,
                                std::vector<std::string> *tokensOut)
{
    const char *delimiters = " \f\n\r\t\v";

    std::istringstream stream(input);
    std::string line;

    while (std::getline(stream, line))
    {
        size_t prev = 0, pos;
        while ((pos = line.find_first_of(delimiters, prev)) != std::string::npos)
        {
            if (pos > prev)
                tokensOut->push_back(line.substr(prev, pos - prev));
            prev = pos + 1;
        }
        if (prev < line.length())
            tokensOut->push_back(line.substr(prev, std::string::npos));
    }
}

bool HexStringToUInt(const std::string &input, unsigned int *uintOut)
{
    // Simple validity check
    if (input[0] != '0' || input[1] != 'x' ||
        input.find_first_not_of("0123456789ABCDEFabcdef", 2) != std::string::npos)
    {
        return false;
    }

    std::stringstream inStream(input);
    inStream >> std::hex >> *uintOut;
    return !inStream.fail();
}

bool ReadFileToString(const std::string &path, std::string *stringOut)
{
    std::ifstream inFile(path.c_str());
    std::string str;

    inFile.seekg(0, std::ios::end);
    str.reserve(static_cast<std::string::size_type>(inFile.tellg()));
    inFile.seekg(0, std::ios::beg);

    str.assign(std::istreambuf_iterator<char>(inFile), std::istreambuf_iterator<char>());
    return !inFile.fail();
}

}
