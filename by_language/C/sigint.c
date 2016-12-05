#include <signal.h>  // for signal(), SIGINT
#include <stdio.h>   // for puts()
#include <unistd.h>  // for pause()
//#include <stdlib.h>  // for exit()

void quit();

int main() {
   puts("Hit Ctrl-C to quit.");
   signal(SIGINT, quit);
   pause();

   return 0;
}

void quit() {
   // use carriage return to overwrite "^C".
   puts("\rGoodbye!");
   //exit(0);
}
