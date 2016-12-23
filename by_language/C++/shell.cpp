// I'll be starting off with basic C, but with the idea of 
// A ridiculously simple shell
// adopting C++ features as quickly as possible

#include <iostream>
#include <stdlib.h>

int main()
{
   std::string command = "";

   // Print welcome message
   std::cout << "Welcome to Simple Shell. Type \"exit\" to quit."
             << std::endl;

   // Main REPL
   while (command != "exit")
   {
      std::cout << "> ";
      std::getline(std::cin, command);

      // Parse command for shell built-ins
      if (command == "exit")
      {
         std::cout << "Goodbye!" << std::endl;
         return 0;
      }
      else
      {
         // XXX Unsafe
         system(command.c_str());
      }
   }
}

