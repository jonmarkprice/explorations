#include <unistd.h>
#include <stdio.h>
#include <string.h>

// A simple test of read
int main() {

   int stdin_fd = 0;
   size_t count = 128;
   char buffer [128];
   ssize_t bytes;

   // initalize the buffer
   memset(buffer, 0, count);

   for (;;)
   {
      usleep(1000);
      bytes = read(0, buffer, count);
      if (bytes > 0)
      {
         printf("Read: %s", buffer);
      }

      // clear buffer
      memset(buffer, 0, count);
   }

}
