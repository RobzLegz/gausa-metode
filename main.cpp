#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    char chars[6] = {'x', 'y', 'z', 't', 'v', 'u'};

    int rows;

    cout << "Enter rows: ";
    cin >> rows;

    int cols = rows + 1;

    int matrix[rows][cols];

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            cout << "Enter " << chars[j] << i + 1 << ": ";
            cin >> matrix[i][j];
        }
        int p_i = 0;
        while (p_i < rows)
        {
            cout << matrix[i][p_i];

            if (p_i == rows - 1)
            {
                cout << chars[p_i];
            }
            else
            {
                cout << chars[p_i] << " + ";
            }

            p_i++;
        }
        cout << " = ";
        int val = 0;
        cin >> val;
        matrix[i][cols] = val;
    }

    cout << "Matrix:" << endl;

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols - 1; j++)
        {
            cout << matrix[i][j] << " ";
        }

        cout << "| " << matrix[i][cols];
        cout << endl;
    }

    return 0;
}