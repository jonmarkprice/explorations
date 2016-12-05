#include <stdio.h>
#include <string.h> // for memset
#include <unistd.h> // for usleep
#include <signal.h> // for signal
#include <stdlib.h> // for exit
#include <assert.h>

// Now, let's make it bounce back and forth
int main() {
   const unsigned short width = 20;
   const char marker = '*';
   unsigned int t = 100000; // 100 millisecond (1/10) second
   char line [width + 1];

   // fill initial indicies 0-19 
   memset(line, ' ', width);
   line[width] = '\0'; // add terminator
   line[0] = marker; 
   
   printf("Waiting %d microseconds between symbols\n", t);
   puts("Hit Ctrl-\\ to quit.");
   
   // print a "frame"
   short i;
   for (i = 0; i < 20; i++) {
      putchar('.');
   }
   putchar('\n');
   
   signal(SIGQUIT, quit);

   while (1) {
      short i;
      
      // print init state
      printf("\r%s", line);

      for (i = 0; i < width - 1; i++) {
         usleep(t);
         line[i] = ' '; // clean up the old marker
         line[i + 1] = marker;
         printf("\r%s", line);
         fflush(stdout);
      }

      // we now have indices 0-18 filled with spaces, with index 19
      // containing a null character.
      // starting with index 18, move the character "down" by writing
      // null characters to 18, 17, ..., 1, 0. (19 times)

      for (i = width - 1; i > 0; i--) {
         //assert(i <= 18);
         assert(i >= 0);
         
         usleep(t);
         line[i] = ' ';
         line[i - 1] = marker;
         printf("\r%s", line);
         fflush(stdout);
      }
   }
   printf("\n");
   return 0;
}

void quit() {
   puts("\b\b  \nGoodbye!");
   exit(0);
}
