int len(int n)
{
    int d = 0;
    int r = n;
    while (r != 0)  //Loops through the number with division by 10 until this division leaves no result
                    // and keeps count of iterations
    {
        r /= 10;
        d++;
    }
    return d;
}

int index(int n, int i)
{
    int d;
    int r = n;
    if (i >= 0)             //Converts positive indexes into negative ones, which are easier to deal with
    {
        i += len(n) * (-1);
    }

    int x = 1;
    while (i * (-1) >= x)   //Loops through the number with modulo 10 to extract last digit, then divides by 10
                            //to discard last digit
    {
        d = r % 10;
        r /= 10;
        x++;
    }
    return d;
}

int poweroften(int exp)
{
    int r = 1;
    int i;
    for (i = 0; exp > i; i++)
    {
        r *= 10;
    }
    return r;
}

int slice(int n, int s1, int s2)
{
    int r = 0;
    if (s2 > s1)            //Rejects input where the first slice index is smaller than the second 
    {
        int current_index = s2 -1;
        int i = 0;
        int new_number;
        while (current_index >= s1)
        {
            new_number = index(n, current_index);
            r += new_number * poweroften(i);
            i++;
            current_index--;
        }
    }
    if (s2 == s1)
    {
        r = index(n, s2);
    }
    return r;
}
