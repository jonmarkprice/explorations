#include <stdio.h>
#include <unistd.h>

// TODO: how can I make it poll?
int main() {

   // It waits for getchar() before printing...
   //getchar();
   //puts("...");
   
   try1();

}

void try1() {
   read(); //fd: int, buff: void*, count: size_t
   puts("...");
}

