#!/usr/bin/python3
"""
This is a cmd file
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    the class
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        exit
        """
        return True

 #   def do_help(self):
 #       """
  #      this is a help command
   #     """
    #    pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
