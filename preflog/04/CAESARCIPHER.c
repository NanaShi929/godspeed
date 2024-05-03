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
 
