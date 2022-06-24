#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_SIZE 101

char *read_string(char *what_to_do) {
    /* Reads a string entered by user, copies it into an appropriately sized dynamic array, 
     * and returns pointer to that array */
    char *buffer = malloc(sizeof(char) * MAX_SIZE);
    for (int i = 0; i < MAX_SIZE - 1; i++) buffer[i] = 'X';
    buffer[MAX_SIZE - 1] = '\0';
    printf("Provide %s (up to %d letters, rest will be truncated): ", what_to_do, MAX_SIZE - 1);
    fflush(stdin);
    fgets(buffer, MAX_SIZE, stdin);
    int l = strlen(buffer);
    char *new = malloc(sizeof(char) * l);
    strncpy(new, buffer, l);
    new[l-1] = '\0'; // fgets() will capture a training line break from enter key; setting that to null
    printf("String length: %d\n", strlen(new));
    free(buffer);
    return new;
}

int letter_checker(char *source) {
    /* Checks a string for validity: Returns 1 if invalid (because string contains) 
     * non-letter character), returns 0 if valid */
    int n = strlen(source);
    for (int i = 0; i < n; i++) {
        int c = source[i];
        if ((c < 65) && (c != 10)) return 1;
        if (c > 122) return 1;
        if ((c > 90) && (c < 97)) return 1;
    }
    return 0;
} 

void uppercase(char *source) {
    /* Converts all lower case characters in string provided to
    upper case ones */
    int n = strlen(source);
    for (int i = 0; i < n; i++) {
        int c = source[i];
        if ((c > 96) && (c < 123)) source[i] -= 32;
    }
} 

char process_one_letter(char letter_in, char key_letter, int mode) {
    /* Encrypts (mode 1) or decrypts (mode 0) one character 
     * Takes one character from input message, one character from key,
     * and mode as parameters */
    int shift = key_letter - 'A';
    char letter_out;
    if (mode) letter_out = letter_in + shift;
    else letter_out = letter_in - shift;
    if (letter_out > 90) letter_out -= 26;
    if (letter_out < 65) letter_out += 26;
    return letter_out;
}


int main(void) {
    
    /* input_to_get and output_produced are not user-provided raw data but
     * simply strings to be printed in user interface 
     * Also some helper variables */
    char *input_to_get = malloc(sizeof(char) * 25);
    input_to_get[0] = '\0';
    char *output_produced = malloc(sizeof(char) * 27);
    output_produced[0] = '\0';
    int mode = 2;
    int end = 0;
    char mode_letter;
    
    while (1) { // Main part of program; calls various helper functions
        printf("E to encode, D to decode, Q to quit: \n");
        scanf("%c", &mode_letter); // User choice of desired mode
        
        if ((mode_letter == 69) || (mode_letter == 101)) { //Encrypting
            mode = 1;
            strcpy(input_to_get, "plain text message\0");
            strcpy(output_produced, "encrypted message message\0");
        }
        else if ((mode_letter == 68) || (mode_letter == 100)) { //Decrypting
            mode = 0;
            strcpy(input_to_get, "encrypted message\0");
            strcpy(output_produced, "decrypted message\0");
        }
        else if ((mode_letter == 81) || (mode_letter == 113)) { // Quitting
            end = 1;
            break;
        }
        else { //User made invalid choice
            printf("Invalid selection.");
            continue;
        }
    
        if (end) return 0;
        
        char *key = read_string("key"); // Get key from user
        int keylen = strlen(key);
        char *mess_in = read_string(input_to_get); // Get input message from user
        uppercase(key);
        uppercase(mess_in);
        
        int n = strlen(mess_in);
        char* mess_out = malloc(sizeof(char) * n + 1); // Buffer for output message
        int j = 0;
        
        for (int i = 0; i < n; i++) { // Convert input message character by character
            if ((mess_in[i] > 64) && (mess_in[i] < 91)) {
                char key_char = key[j % keylen];
                mess_out[i] = process_one_letter(mess_in[i], key_char, mode);
                j++; /* Separate variable because key character does not proceed if a non-letter
                character is encountered in input message */
            }
            else mess_out[i] = mess_in[i];
        }
        mess_out[n] = '\0';
        printf("%s: %s\n\n", output_produced, mess_out); // Display result
        
        free(key);
        free(input_to_get);
        free(mess_in);
        free(mess_out);
        free(output_produced);
    } 
    return 0;
}
