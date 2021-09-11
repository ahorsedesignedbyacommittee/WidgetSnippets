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
    if (i < 0)
    {
        ;
    }
    else                    //Converts positive indexes into negative ones, which are easier to deal with
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
