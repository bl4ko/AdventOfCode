#include <stdio.h>
#include <string.h>

int main() {
    FILE* input = fopen("input.txt", "r");
    int num;
    char* word;
    int horizontal = 0, depth = 0, aim = 0; 
    while (fscanf(input, "%s %d", word, &num) != EOF) {
            if (strcmp(word, "forward") == 0) {
                horizontal += num;
                depth += aim * num;
            }
            else if (strcmp(word, "down") == 0) 
                aim += num;
            else 
                aim -= num;
    }
    fclose(input);
    printf("%d\n", horizontal * depth);
}