int len(int n)
{
    int d = 0;
    int r = n;   
    while (r != 0) //Loops through the number with division by 10 until this division leaves no result > 10
    {
        r /= 10;
        d++;
    }
    return d;
}
