#include <stdio.h>
#include <string.h> // for memset
#include <unistd.h> // for usleep

// Make the a character move
int main() {
   const unsigned short len = 20;
   unsigned int t = 100000; // 100 millisecond (1/10) second
   short i;
   char padding [len];

   // nec?
   memset(padding, '\0', len);

   printf("Waiting %d microseconds between symbols\n", t);

   for (i = 0; i < len; i++) {
      usleep(t);
      
      // for fun, use memset instead of a nested loop
      // printing spaces:
      // memset(padding, ' ', i);
      // ... Actually, only 1 space is changing... so:
      if (i > 0) padding[i - 1] = ' ';

      printf("%s*\r", padding);

      // If we don't flush, the program will wait until all
      // either a newline or the end of the program to
      // actually display the output.
      fflush(stdout);
   }

   printf("\n");
   return 0;
}
