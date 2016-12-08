#include <stdio.h>

void a(const char *const);

int main()
{
   const char *const x = "Hello";
   a(x);

   return 0;
}

void a(const char *const x)
{
   // OK
   const char *const words[] = {"Hi", x, "Dog"};

   // XXX: Warning: "Initalization discards const qaulifier from 
   // pointer target type"
   char *const more[] = {x, "Pizza"};
   
   // Why does this bring up a warning? 
   // The type char *const indicates that the pointer (to a a
   // character) should not be allowed to change, but how am I
   // changing the pointer?
   //
   // more --> [0][1]
   //           |  |
   //           |  `---> [H][e][l][l][o]
   //           `------> [P][i][z][z][a]
   //                     ^
   //                     |
   // x ------------------'
   //
   // Are we actually *changing* the x pointer, or are we simply
   // making another thing point to it?
   //
   // TODO: Try to break it. If I *can* in some way modify
   // the value (through the pointer), then it isn't right

   // This issues more warnings, but still allows us to change the 
   // array.
   char *p = more;
   p[0] = "A";
   int i;
   for (i = 0; i < 2; i++) {
      printf("%s\n", more[i]);
   }


   // printf("%c\n", *x);

   // OK
   const char *even_more[] = {"One" "Two", x};
}

