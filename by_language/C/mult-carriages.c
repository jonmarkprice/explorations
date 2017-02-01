// Can i do multiple carriage returns in a row?
#include <stdio.h>

int main()
{
   puts("First line ...");
   puts("Second line ...");
   fflush(stdout);

   puts("\b\b\b\bFirst line again");

   return 0;
}
