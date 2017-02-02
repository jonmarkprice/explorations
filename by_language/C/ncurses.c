#include <ncurses.h>

// the Hello World program for ncurses from Pradeep Padala's HOWTO
int main()
{
   initscr();
   printw("Hello world!");
   refresh();
   getch();
   endwin();

   return 0;
}
