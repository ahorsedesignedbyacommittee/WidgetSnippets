#include <stdio.h>

// Function prototypes
int check_valid_input(int y, int m, int d, int *month_lengths);
int leap_year_checker(int y);
int zeller(int y, int m, int d);
void spencer(int y, int *easter_day_ptr, int *easter_month_ptr);

int main(void) {
    
    int y, m, d;
    char again;
    char *weekdays[] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    char *months[] = {"None", "January", "February", "March", "April", "May"};
    int easter_day, easter_month;
    
    while (1) {
        
        // Get input: year, month, day
        printf("Year: "); scanf("%d", &y);
        printf("Month: "); scanf("%d", &m);
        printf("Day: "); scanf("%d", &d);
        
        // Call checker functions
        int month_lengths[] = {0, 31, leap_year_checker(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (check_valid_input(y, m, d, month_lengths)) continue;
        
        // Calculate and display number of day in the year
        int day_in_year = 0;
        for (int i = 0; i < m; i++) day_in_year += month_lengths[i];
        day_in_year += d;
        printf("Date in question is a %s. Day #%d in the course of the year.\n", weekdays[zeller(y,m,d)], day_in_year);
        
        // Display if it was leap year, call Spencer function to determine date of Easter and display it
        if (month_lengths[2] == 29) printf("Leap year.\n");
        else printf("Not a leap year.\n");
        spencer(y, &easter_day, &easter_month);
        printf("Easter in %d: %d %s\n\n", y, easter_day, months[easter_month]);
        
        
        // Repeat loop if desired, otherwise exit
        printf("Again? (Y to check other date) "); scanf(" %c", &again);
        if ((again != 'Y')&&(again != 'y')) break;
    }
    return 0;
}


int check_valid_input(int y, int m, int d, int *month_lengths) {
    //Returns 0 if date entered is valid, 1 otherwise
    if (y < 1583) { // 15 October 1582 as starting point of Gregorian Calendar
        printf("Invalid year: Program supports only years from 1583 onwards.\n");
        return 1;
    }
    
    if ((m < 0)||(m > 12)) {
        printf("Invalid month: Must be 1-12 inclusive.\n");
        return 1;
    }
        
    
    if (d > month_lengths[m]) {
        printf("Invalid date: No such day in this month.\n");
        return 1;
    }
    return 0;
}

int leap_year_checker(int y) {
    // Returns 29 if year is leap year, 28 otherwise
    if (!(y % 400)) return 29;
    if (!(y % 100)) return 28;
    if (!(y % 4)) return 29;
    return 28;
}

int zeller(int y, int m, int d) {
    // Uses Zeller's Congruence to determine day of week for a given date and returns it
    if (m < 3) m += 12;
    int k = y % 100;
    int j = y / 100;
    int x1 = ((m+1)*13)/5;
    int h = (d + x1 + k + k/4 + j/4 + 5*j) % 7;
    return h;
}

void spencer(int y, int *easter_day_ptr, int *easter_month_ptr) {
    /* Uses Spencer's  easter algorithm to determine day and month of Easter of the given year;
    stores these results under pointers provided by main function */
    int a = y % 19;
    int b = y / 100;
    int c = y % 100;
    int d = b / 4;
    int e = b % 4;
    int f = (b + 8) / 28;
    int g = (b - f + 1) / 3;
    int h = (19*a + b - d - g + 15) % 30;
    int i = c / 4;
    int k = c % 4;
    int l = (32 + 2*e + 2*i + - h - k) % 7;
    int m = (a + 11*h + 22*l) / 451;
    int n = (h + l - 7*m + 114) / 31;
    int o = (h + l - 7*m + 114) % 31;
    
    *easter_day_ptr = o + 1;
    *easter_month_ptr = n;
    return;
}
