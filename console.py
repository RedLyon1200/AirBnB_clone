#!/usr/bin/python3
"""[contains the entry point of the command interpreter]
"""
import cmd
import models
from models.base_model import BaseModel
from models import classes
import shlex


class HBNBCommand(cmd.Cmd):
    """[This is the htbn cls]
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
        """quit: quit
    Quit the console.

    Quits the console with not status.

    Exit Status:
    Returns true whenever the quit signal is detected."""
        return True

    def do_EOF(self, arg):
        """EOF: ^C
    Exit the console.

    Exits the console with not status.

    Exit Status:
    Returns true each time the keyboard interrupt signal is detected."""
        return True

    """ def do_help(self, arg):
        print(arg) """

    def do_create(self, arg):
        """create: create CLASS_NAME
    Instantiate classes

    Creates a new instance of CLASS_NAME, saves it (to the JSON file) and \
print the id. """
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
        """show: show CLASS_NAME ID
    Show classes

    Prints the string representation of an instance based on the CLASS_NAME \
and ID."""
        args = arg.split()

        if self.validate_args(args):
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if self.validate_id(stored_dict, key):
                print(stored_dict[key])

    def do_destroy(self, arg):
        """destroy: destroy CLASS_NAME ID
    Remove classes

    Deletes an instance based on the CLASS_NAME and ID (save the change into \
the JSON file)."""
        args = arg.split()

        if self.validate_args(args):
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if self.validate_id(stored_dict, key):
                del stored_dict[key]
                models.storage.save()

    def do_all(self, arg):
        """all: all [class_name]
    See classes

    Prints all string representation of all instances based or not on the \
[class_name].

    Options:
      class_name    shows only the information of said class."""
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
        """update: update CLASS_NAME ID ATTR_NAME ATTR_VALUE
    Update classes

    Updates an instance based on the CLASS_NAME and ID by adding or updating \
the ATTR_NAME (the change is saved in the JSON file)."""
        args = shlex.split(arg)

        if self.validate_args(args, update=True):
            attr = args[2]
            value = args[3]

            if attr in ['id', 'created_at', 'update_at']:
                return
            stored_dict = models.storage.all()
            key = args[0] + '.' + args[1]
            if self.validate_id(stored_dict, key):
                setattr(stored_dict[key], attr, value)
                print(stored_dict[key])
                models.storage.save()

    def validate_id(self, stored_dict, id):
        """validate_id: validate_id(STORED_DICT, ID)
    Review id

    Validate if the STORED_DICT contains the ID.

    Exit Status:
    Returns true if ARGS is correct, otherwise returns False."""

        if id in stored_dict:
            return True
        else:
            print(self.errors['id_not_found'])
            return False

    def validate_args(self, args, update=False):
        """validate_args: validate_args(ARGS, [update])
    Check arguments

    Validates the amount and type of ARGS sent and optionally, check or not \
the validations of the [update].

    Exit Status:
    Returns true if ARGS is correct, otherwise returns False."""
        if len(args) < 1:
            print(self.errors['empty'])
        elif args[0] not in classes:
            print(self.errors['no_cls'])
        elif len(args) < 2:
            print(self.errors['no_id'])
        elif update:
            if len(args) < 3:
                print(self.errors['no_attr'])
            elif len(args) < 4:
                print(self.errors['no_val'])
            else:
                return True
        else:
            return True

        return False

    def emptyline(self):
        """emptyline:
    empty line

    if an empty line is sent through ENTER the program does nothing."""
        pass


if __name__ == "__main__":
    """main entry"""
    HBNBCommand().cmdloop()
