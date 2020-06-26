#!/usr/bin/python3
"""[contains the entry point of the command interpreter]
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """[This is the htbn cls]

    Args:
        cmd ([Cmd])
    """
    prompt = '(hbtn) '
    classes = ['BaseModel']
    errors = {
        'empty': '** class name missing **',
        'no_exist': '** class doesn\'t exist **',
        'no_id': '** instance id missing **',
        'id_not_found': '** no instance found **'
    }

    def do_quit(self, arg):
        """[Quit command to exit the console]"""
        return True

    def do_EOF(self, arg):
        """[Exit the console]"""
        return True

    def do_create(self, arg):
        args = arg.split()

        if len(args) < 1:
            print(self.errors['empty'])
        elif args[0] not in self.classes:
            print(self.errors['no_exist'])
        else:
            if args[0] == 'BaseModel':
                obj = models.base_model.BaseModel()

        obj.save()
        print('{}'.format(obj.id))

    def do_show(self, arg):
        args = arg.split()

        if len(args) < 1:
            print(self.errors['empty'])
        elif args[0] not in self.classes:
            print(self.errors['no_exist'])
        elif len(args) < 2:
            print(self.errors['no_id'])
        else:
            models.storage.reload()
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in stored_dict:
                print(self.errors['id_not_found'])
            else:
                print(stored_dict[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
