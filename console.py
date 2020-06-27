#!/usr/bin/python3
"""[contains the entry point of the command interpreter]
"""
import cmd
import models
from models.base_model import BaseModel
from models import classes


class HBNBCommand(cmd.Cmd):
    """[This is the htbn cls]

    Args:
        cmd ([Cmd])
    """
    prompt = '(hbtn) '
    errors = {
        'empty': '** class name missing **',
        'no_cls': '** class doesn\'t exist **',
        'no_id': '** instance id missing **',
        'id_not_found': '** no instance found **',
        'no_attr': '** attribute name missing **',
        'no_val': '** value missing **'
    }

    def do_quit(self, arg):
        """[Quit command to exit the console]"""
        return True

    def do_EOF(self, arg):
        """[Exit the console]"""
        return True

    def do_create(self, arg):
        """[Create a specified model]
        """
        args = arg.split()

        if len(args) == 0:
            print(self.errors['empty'])
        elif args[0] not in classes:
            print(self.errors['no_cls'])
        else:
            obj = classes[args[0]]()

            print('{}'.format(obj.id))
            obj.save()

    def do_show(self, arg):
        """[Show model]"""
        args = arg.split()

        if self.validate_args(args):
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in stored_dict:
                print(self.errors['id_not_found'])
            else:
                print(stored_dict[key])

    def do_destroy(self, arg):
        """[Destroy model]
        """
        args = arg.split()

        if self.validate_args(args):
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in stored_dict:
                print(self.errors['id_not_found'])
            else:
                del stored_dict[key]
                models.storage.save()

    def do_all(self, arg):
        """[Print all instances]
        """
        args = arg.split()
        instances = []

        if len(args) == 0:
            for value in models.storage.all().values():
                instances.append(str(value))
            print(instances)
        elif args[0] in classes:
            for keys in models.storage.all():
                if args[0] in keys:
                    instances.append(str(models.storage.all()[keys]))
            print(instances)
        else:
            print(self.errors['no_cls'])

    def do_update(self, arg):
        args = arg.split()

        if self.validate_args(args, update=True):
            attr = args[2]
            value = args[3]

            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if key not in stored_dict:
                print(self.errors['id_not_found'])
            else:
                setattr(stored_dict[key], attr, value)
                print(stored_dict[key])
                models.storage.save()

    def validate_args(self, args, update=False):
        """[Validate arguments]
        """
        if len(args) < 1:
            print(self.errors['empty'])
        elif args[0] not in classes:
            print(self.errors['no_cls'])
        elif len(args) < 2:
            print(self.errors['no_id'])
        else:
            if update:
                if len(args) < 3:
                    print(self.errors['no_attr'])
                elif len(args) < 4:
                    print(self.errors['no_val'])
                else:
                    return True
            else:
                return True

    def emptyline(self):
        """[pass if command is empty]
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
