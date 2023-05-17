#!/usr/bin/python3
"""
This is a cmd file
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    the class
    """

    prompt = '(hbnb) '

    classes = {"BaseModel": BaseModel, "User": User}

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

    def emptyline(self):
        """
        Do nothing
        """
        pass

    def do_create(self, class_name):
        """
        creates a new instance of base model
        """
        if class_name == '':
            print("** class name missing **")

        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            my_model = HBNBCommand.classes[class_name]()
            print(my_model.to_dict()['id'])
            my_model.save()

    def do_show(self, args):
        """
        shows
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** exist **")
            else:
                print("** instance id missing **")
        else:
            class_name, class_id = args
            obj_all = storage.all()

            key = "{}.{}".format(class_name, class_id)
            if key in obj_all:
                data = obj_all[key]
                my_model = HBNBCommand.classes[class_name](**data)
                print(my_model)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        destroys
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            class_name, class_id = args
            obj_all = storage.all()

            key = "{}.{}".format(class_name, class_id)

            if key in obj_all:
                del obj_all[key]
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, class_name):
        """
        list all instances
        """
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

        else:
            list_ = []
            obj_all = storage.all().copy()

            for value in obj_all.values():
                my_model = HBNBCommand.classes[class_name](**value)
                list_.append(my_model.__str__())
            print(list_)

    def do_update(self, args):
        """
        updates a entry
        """
        args = args.split()

        if len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            print("** instance id missing **")

        elif len(args) == 2:
            print("** attribute name missing **")

        elif len(args) == 3:
            print("** value missing **")

        else:

            class_name, class_id, attr_name, attr_value = args
            obj_all = storage.all()

            key = "{}.{}".format(class_name, class_id)

            if key in obj_all.keys():
                obj_all[key][attr_name] = str(attr_value)

            else:
                print("** no instance found **")

        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
