#include <iostream>
#include <fstream>;
#include <string>;
#include <cstring>;
#include <vector>;
#include <map>;
#include <algorithm>;

using namespace std;

int getIndexAndRemove(vector<char>* v, char K)
{
    for (int i = v->size() - 1; i >= 0; i--) {
        if ((*v)[i] == K) {
            v->erase(v->begin() + i);
            return i;
        }
    }
    return -1;
}

int main() 
{
    map<char, char> m = {
    {')', '('},
    {'}', '{'},
    {']', '['},
    {'>', '<'},
    };
    map<char, int> mPoints = {
        {'(', 1},
        {'{', 3},
        {'[', 2},
        {'<', 4},
    };
    vector<long long int> sums;

    fstream MyReadFile("brackets.txt");
    string line;
    while (getline(MyReadFile, line))
    {
        vector<char> v;
        for (int i = 0; i < line.length(); i++) 
        {
            string opening = "({[<";
            if (opening.find(line[i]) < opening.length()) v.push_back(line[i]);
            else 
            {
                getIndexAndRemove(&v, m[line[i]]);
            }
        }

        long long int sum = 0;
        for (int j = v.size() - 1; j >= 0; j--) 
        {
            sum *= 5;
            sum += mPoints[v[j]];
        }
        cout << sum << endl;
        
        sums.push_back(sum);
    }

    sort(sums.begin(), sums.end());
    for (int i = 0; i < sums.size(); i++) cout << sums[i] << endl;
    cout << sums[sums.size() / 2];
    MyReadFile.close();
}