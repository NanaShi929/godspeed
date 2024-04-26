// #include <stdio.h>
// int main() {
// int i, f;
// char pop[100], c;
// printf("Enter a plaintext: \n");
// fgets(pop, sizeof(pop), stdin);
// printf("Enter key: ");
// scanf("%d", &f);
// for (i = 0; pop[i] != '\0'; i++) {
// c = pop[i];
// if (c >= 'a' && c <= 'z') {
// c = c -f;//"-" for decryption
// // Handle wrapping around for lowercase letters
// c = (c - 'a') % 26 + 'a';
// } else if (c >= 'A' && c <= 'Z') {
// c = c - f; //"-" for decryption
// // Handle wrapping around for uppercase letters
// c = (c - 'A') % 26 + 'A';
// }
// pop[i] = c;
// }
// printf("Encrypted message: %s", pop);
// return 0;
// }
#include<stdio.h>

#include<ctype.h>

int main() {

    char text[500], ch;

    int key;

    // Taking user input.
    printf("Enter a message to encrypt: ");

    scanf("%s", text);

    printf("Enter the key: ");

    scanf("%d", & key);

    // Visiting character by character.

    for (int i = 0; text[i] != '\0'; ++i) {

        ch = text[i];
        // Check for valid characters.
        if (isalnum(ch)) {

            //Lowercase characters.
            if (islower(ch)) {
                ch = (ch - 'a' + key) % 26 + 'a';
            }
            // Uppercase characters.
            if (isupper(ch)) {
                ch = (ch - 'A' + key) % 26 + 'A';
            }

            // Numbers.
            if (isdigit(ch)) {
                ch = (ch - '0' + key) % 10 + '0';
            }
        }
        // Invalid character.
        else {
            printf("Invalid Message");
        }

        // Adding encoded answer.
        text[i] = ch;

    }

    printf("Encrypted message: %s", text);

    return 0;
}