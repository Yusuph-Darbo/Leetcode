// Approach:
// Iterate from 1 to n and add numbers not divisible by m to total1.
// Add divisible numbers to total2, then return their difference.
//
// Time: O(n)
// Space: O(1)

int differenceOfSums(int n, int m)
{
    int total1 = 0;
    int total2 = 0;

    for (int i = 1; i <= n; i++)
    {
        if (i % m != 0)
        {
            total1 += i;
        }
        else
        {
            total2 += i;
        }
    }

    return total1 - total2;
}