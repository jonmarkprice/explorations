#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Got error: "variably modified 'string' at file scope".
// Even using 'const', but it goes away with #define.
// const size_t STR_SIZE = 10;

#define STR_SIZE (10)

struct item
{
   enum datatype {NUMBER, STRING, LOGICAL} type;
   union value {
      int number;
      char string [STR_SIZE];
      bool logical;
   } data;
};

void printItem(struct item);

int main()
{
   struct item x;
   x.type = NUMBER;
   x.data.number = 3;

   struct item y;
   y.type = STRING;
   strcpy(y.data.string, "Hello");

   struct item z;
   z.type = LOGICAL;
   z.data.logical = true;
   //printf("Number: %d\n", x.data.number);
   //printf("Word: \"%s\"\n", y.data.string);

   printItem(x);
   printItem(y);
   printItem(z);

   return 0;
}

void printItem(struct item x)
{
   char* names [] = {"False", "True"};
   switch(x.type)
   {
      case NUMBER:
         printf("The number %d.\n", x.data.number);
         break;
      case STRING:
         printf("The string \"%s\".\n", x.data.string);
         break;
      case LOGICAL:
         printf("The boolean %s.\n", names[x.data.logical]);
         break;
      default:
         puts("An unknown type!");
   }
}

