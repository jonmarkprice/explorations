// A one-dimensional life
#include <stdio.h>
#include <unistd.h>

int main()
{
   // TODO:
   // n time, instead of bool arrays, use unsigned ints/shorts, etc
   // and boolean arithmetic
   const size_t width = 5;
   bool current [width];
   short count [width];
   bool next [width];
   int i;
   for (i = 0; i < width - 1; i++)
   {  
      char temp;
      if (i > 0)
      {
         temp += (char) current[i - 1]
      }
      temp += (char) current[i];
      if (i < width - 1)
      {
         temp += (char) current[i + 1];
      }
      count[i] = temp;

      //
   }     
      // this is a bad approach, just count neighbors 
      // six cases
      if (current[i]) //alive
      {
       /*
       * n = 0, 1, 2
       *    0: die
       *    1: stay alive
       *    2: die
       *
       * if dead
       *    0: stay dead
       *    1: stay dead
       *    2: come alive
       *
       */
      if (i == 0)
      {
         if (c[i + 1])
         {
            n[i] = true
         }
         else 
         {
            n[i] = false;
         }
      }      

      if (i > 0 && i < width - 2)
      {
         if (c[i - 1] && c[i + 1]) {
            n[i] = !c[i];
         }
         else if (!c[i - 1] && !c[i + 1])
         {
            n[i] = c[i];
         }
         else if (!c[i] && (c[i - 1] || c[i + 1]))
         {
            n[i] = true;
         }
      }

}
