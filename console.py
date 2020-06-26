#!/usr/bin/python3
"""[contains the entry point of the command interpreter]
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """[This is the htbn cls]

    Args:
        cmd ([Cmd])
    """
    prompt = '(hbtn) '

    def do_quit(self, arg):
        """[Quit command to exit the console]"""
        return True

    def do_EOF(self, arg):
        """[Exit the console]"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
