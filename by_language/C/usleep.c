#include <stdio.h> // for puts
#include <unistd.h> // for usleep

int main() {
   const unsigned short len = 20;
   unsigned int t = 100000; // 100 millisecond (1/10) second
   short i;

   printf("Waiting %d microseconds between symbols\n", t);

   for (i = 0; i < len; i++) {
      usleep(t);
      printf("*");

      // If we don't flush, the program will wait until all
      // either a newline or the end of the program to
      // actually display the output.
      fflush(stdout);
   }

   printf("\n");
   return 0;
}
