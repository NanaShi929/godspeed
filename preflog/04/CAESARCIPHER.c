#include <stdio.h>
int main() {
int i, f;
char pop[100], c;
printf("Enter a plaintext: \n");
fgets(pop, sizeof(pop), stdin);
printf("Enter key: ");
scanf("%d", &f);
for (i = 0; pop[i] != '\0'; i++) {
c = pop[i];
if (c >= 'a' && c <= 'z') {
c = c - f;//"+" for encryption
//c= c+f;
if (c > 'z') {
c = c - 'z' + 'a' - 1;
}
pop[i] = c;
} else if (c >= 'A' && c <= 'Z') {
c = c - f;//"+" for encryption
//c= c+f;
if (c > 'Z') {
c = c - 'Z' + 'A' - 1;
}
pop[i] = c;
}
}
printf("Encrypted message: %s", pop);
return 0;
}

// //Caesar cipher:-
// //It's a type of substitution cipher where each letter in the plaintext is replaced by a letter a certain number of positions down the alphabet. For example, with a shift of 3, "hello" would become "khoor."
// #include<stdio.h>

// #include<ctype.h>

// int main() {

//     char text[500], ch;

//     int key;

//     // Taking user input.

//     printf("Enter a message to decrypt: ");

//     scanf("%s", text);

//     printf("Enter the key: ");

//     scanf("%d", & key);

//     // Visiting each character.
//     for (int i = 0; text[i] != '\0'; ++i) {

//         ch = text[i];
//         // Check for valid characters.
//         if (isalnum(ch)) {
//             //Lowercase characters.
//             if (islower(ch)) {
//                 ch = (ch - 'a' - key + 26) % 26 + 'a';
//             }
//             // Uppercase characters.
//             if (isupper(ch)) {
//                 ch = (ch - 'A' - key + 26) % 26 + 'A';
//             }
//             // Numbers.
//             if (isdigit(ch)) {
//                 ch = (ch - '0' - key + 10) % 10 + '0';
//             }
//         }
//         // Invalid characters.
//         else {
//             printf("Invalid Message");
//         }
//         // Adding decoded character back.
//         text[i] = ch;

//     }

//     printf("Decrypted message: %s", text);

//     return 0;

// }