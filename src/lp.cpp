#include "bits/stdc++.h"
using namespace std;
int north[16];
int south[16];
int west[16];
int east[16];
int mapping[4][4];
float A[16][16][4];
float reward[16];
// 0 - North
// 1 - South
// 2 - West
// 3 - East

// 0, 3, 14 are goal states.
// 1, 10 are walls.
// We skip the above states.
bool isWall(int state)
{
    if(state == 1 || state == 10)
        return true;
    return false;
}

int main()
{
    float team_number = 33;
    float step_cost = -team_number / 10;
    reward[0] = team_number / 10;
    reward[3] = team_number;
    reward[14] = - team_number / 5;
    for(int i = 0; i < 16; ++i)
    {
        if(reward[i] == 0)
            reward[i] = step_cost;
    }

    int cnt = 0;
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            mapping[i][j] = cnt++;
        }
    }
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            if((i - 1) >= 0)
                north[mapping[i][j]] = mapping[i - 1][j];
            if((i + 1) < 4)
                south[mapping[i][j]] = mapping[i + 1][j];
            if((j - 1) >= 0)
                west[mapping[i][j]] = mapping[i][j - 1];
            if((j + 1) < 4)
                east[mapping[i][j]] = mapping[i][j + 1];
        }
    }

    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            if(mapping[i][j] == 0 || mapping[i][j] == 3 || mapping[i][j] == 14 || mapping[i][j] == 1 || mapping[i][j] == 10)
                continue;
            // Consider the north
            if((i - 1) >= 0 && !isWall(mapping[i - 1][j])){
                A[mapping[i][j]][mapping[i][j]][0] = 0.8;
                A[mapping[i - 1][j]][mapping[i][j]][0] = -0.8;
            }
            if((j - 1) >= 0 && !isWall(mapping[i][j - 1])){
                A[mapping[i][j]][mapping[i][j]][0] = 0.1;
                A[mapping[i][j - 1]][mapping[i][j]][0] = -0.1;
            }
            if((j + 1) < 4 && !isWall(mapping[i][j + 1])){
                A[mapping[i][j]][mapping[i][j]][0] = 0.1;
                A[mapping[i][j + 1]][mapping[i][j]][0] = -0.1;
            }
            // Consider South
            if((i + 1) < 4 && !isWall(mapping[i + 1][j])){
                A[mapping[i][j]][mapping[i][j]][1] = 0.8;
                A[mapping[i + 1][j]][mapping[i][j]][1] = -0.8;
            }
            if((j - 1) >= 0 && !isWall(mapping[i][j - 1])){
                A[mapping[i][j]][mapping[i][j]][1] = 0.1;
                A[mapping[i][j - 1]][mapping[i][j]][1] = -0.1;
            }
            if((j + 1) < 4 && !isWall(mapping[i][j + 1])){
                A[mapping[i][j]][mapping[i][j]][1] = 0.1;
                A[mapping[i][j + 1]][mapping[i][j]][1] = -0.1;
            }
            // Consider West
            if((j + 1) < 4 && !isWall(mapping[i][j + 1])){
                A[mapping[i][j]][mapping[i][j]][2] = 0.8;
                A[mapping[i][j + 1]][mapping[i][j]][2] = -0.8;
            }
            if((i - 1) >= 0 && !isWall(mapping[i - 1][j])){
                A[mapping[i][j]][mapping[i][j]][2] = 0.1;
                A[mapping[i - 1][j]][mapping[i][j]][2] = -0.1;
            }
            if((i + 1) < 4 && !isWall(mapping[i + 1][j])){
                A[mapping[i][j]][mapping[i][j]][2] = 0.1;
                A[mapping[i + 1][j]][mapping[i][j]][2] = -0.1;
            }
            // Consider East
            if((j - 1) >= 0 && !isWall(mapping[i][j - 1])){
                A[mapping[i][j]][mapping[i][j]][3] = 0.8;
                A[mapping[i][j - 1]][mapping[i][j]][3] = -0.8;
            }
            if((i - 1) >= 0 && !isWall(mapping[i - 1][j])){
                A[mapping[i][j]][mapping[i][j]][3] = 0.1;
                A[mapping[i - 1][j]][mapping[i][j]][3] = -0.1;
            }
            if((i + 1) < 4 && !isWall(mapping[i + 1][j])){
                A[mapping[i][j]][mapping[i][j]][3] = 0.1;
                A[mapping[i + 1][j]][mapping[i][j]][3] = -0.1;
            }
        }
    }
    A[0][0][0] = 1.0;
    A[3][3][0] = 1.0;
    A[14][14][0] = 1.0;
    for(int j = 0; j < 16; ++j)
    {
        for(int k = 0; k < 4; ++k)
            cout << "x" << j << k << "   \t    ";
    }
    cout << endl << endl;
    for(int i = 0; i < 16; ++i){
        for(int j = 0; j < 16; ++j){
            for(int k = 0; k < 4; ++k){
                cout << A[i][j][k] <<"   \t    ";
            }
        }
        cout << endl;
    }
    return 0;
}