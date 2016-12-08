#include <stdio.h>
#include <string.h>
union num
{
   int value;
   char name [10];
};

int main()
{
   union num one;
   one.value = 1;
   // one.name = 'O';

   printf("Number: %d\n", one.value);

   //one.name = "One";
   strcpy(one.name, "One");

   printf("Word \"%s\"\n", one.name);
   return 0;
}

