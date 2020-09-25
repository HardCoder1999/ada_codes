#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int l_min, l_max, b_min, b_max, i, j, x;
    cin >> l_min;
    cin >> l_max;
    cin >> b_min;
    cin >> b_max;

    vector<vector<int> > t(l_max+1, vector<int>(b_max+1, 0));
    int count = 0;

    for(i=1;i<l_max+1;i++)
        t[i][1] = i;
    for(j=1;j<b_max+1;j++)
        t[1][j] = j;

    if(l_min == 1){
        x = (int)(b_max*(b_max+1)/2) - (b_min*(b_min-1)/2);
        count += x;
    }

    if (b_min == 1)
    {
        x = (int)(l_max * (l_max + 1) / 2) - (l_min * (l_min - 1) / 2);
        count += x;
    }

    if(l_min == 1 && b_min == 1)
        count -= 1;

    for(i=2;i<l_max+1;i++)
    {
        for(j=2;j<b_max+1;j++)
        {
            if(i == j)
                t[i][j] = 1;
            else
            {
                if(i < j)
                    t[i][j] = 1 + t[i][j-i];
                else
                    t[i][j] = t[i-j][j] + 1;
            }

            if(i >= l_min && j >= b_min)
                count += t[i][j];
            
        }
    }
    cout << count << endl;
}