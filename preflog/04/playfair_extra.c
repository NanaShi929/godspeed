#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define SIZE 5

char* prepare_input(char* text) {
    int i, j;
    char* filtered_text = (char*)malloc(strlen(text) * sizeof(char));
    int index = 0;
    for (i = 0; i < strlen(text); i++) {
        if (isalpha(text[i])) {
            if (text[i] == 'J')
                text[i] = 'I';
            filtered_text[index++] = toupper(text[i]);
        }
    }
    filtered_text[index] = '\0';
    if (strlen(filtered_text) % 2 != 0) {
        filtered_text[index++] = 'X';
        filtered_text[index] = '\0';
    }
    return filtered_text;
}

void generate_key_matrix(char* key, char key_matrix[SIZE][SIZE]) {
    int i, j, k;
    char alphabet[] = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    strcat(key, alphabet);
    int index = 0;
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            while (strchr(key_matrix[i], key[index]) || key[index] == '\0')
                index++;
            key_matrix[i][j] = key[index];
            index++;
        }
    }
}

void find_position(char key_matrix[SIZE][SIZE], char letter, int* row, int* col) {
    int i, j;
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++) {
            if (key_matrix[i][j] == letter) {
                *row = i;
                *col = j;
                return;
            }
        }
    }
}

void encrypt(char* text, char* key, char key_matrix[SIZE][SIZE], char* encrypted_text) {
    char* filtered_text = prepare_input(text);
    int len = strlen(filtered_text);
    int i, j, index = 0;
    for (i = 0; i < len; i += 2) {
        char letter1 = filtered_text[i];
        char letter2 = filtered_text[i + 1];
        int row1, col1, row2, col2;
        find_position(key_matrix, letter1, &row1, &col1);
        find_position(key_matrix, letter2, &row2, &col2);
        if (row1 == row2)
            encrypted_text[index++] = key_matrix[row1][(col1 + 1) % SIZE];
        else if (col1 == col2)
            encrypted_text[index++] = key_matrix[(row1 + 1) % SIZE][col1];
        else {
            encrypted_text[index++] = key_matrix[row1][col2];
            encrypted_text[index++] = key_matrix[row2][col1];
        }
    }
    encrypted_text[index] = '\0';
    free(filtered_text);
}

void decrypt(char* text, char* key, char key_matrix[SIZE][SIZE], char* decrypted_text) {
    int len = strlen(text);
    int i, j, index = 0;
    for (i = 0; i < len; i += 2) {
        char letter1 = text[i];
        char letter2 = text[i + 1];
        int row1, col1, row2, col2;
        find_position(key_matrix, letter1, &row1, &col1);
        find_position(key_matrix, letter2, &row2, &col2);
        if (row1 == row2)
            decrypted_text[index++] = key_matrix[row1][(col1 - 1 + SIZE) % SIZE];
        else if (col1 == col2)
            decrypted_text[index++] = key_matrix[(row1 - 1 + SIZE) % SIZE][col1];
        else {
            decrypted_text[index++] = key_matrix[row1][col2];
            decrypted_text[index++] = key_matrix[row2][col1];
        }
    }
    decrypted_text[index] = '\0';
}

int main() {
    char key[SIZE*SIZE];
    char key_matrix[SIZE][SIZE];
    char text[100];
    char encrypted_text[100];
    char decrypted_text[100];

    printf("Enter the key (no spaces, all uppercase, J replaced by I): ");
    scanf("%s", key);
    generate_key_matrix(key, key_matrix);

    printf("Enter the text to encrypt: ");
    scanf("%s", text);
    encrypt(text, key, key_matrix, encrypted_text);
    printf("Encrypted: %s\n", encrypted_text);

    decrypt(encrypted_text, key, key_matrix, decrypted_text);
    printf("Decrypted: %s\n", decrypted_text);

    return 0;
}
