#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void quit();

// Like with Ctrl-C program, but this leaves Ctrl-C open for emergencies
int main() {
   puts("Hit Ctrl-\\ to quit.");
   signal(SIGQUIT, quit);
   pause();
   return 0;
}

void quit() {
   puts("\rGoodbye!");
   return;
}
