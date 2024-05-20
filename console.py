#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
class HBNBCommand(cmd.Cmd):

    """
    This class represents the command-line interpreter for the AirBnB clone.
    """
    prompt = "(hbnb) "
    classmodel = {"BaseModel": BaseModel, "User": User}

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Handle EOF (End of File) input
        """
        print("")
        return True

    def help_quit(self):
        """
        Display help message for the quit command
        """
        print("Quit command to exit the program")

    def do_create(self, arg):
        """
        Create a new instance of a specified class
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classmodel:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classmodel[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        print the string representation of an instance
        """
        line = arg.split(" ")
        d = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classmodel:
            print("** class doesn't exist **")
        elif line[0] in HBNBCommand.classmodel and len(line) < 2:
            print("** instance id missing **")
        elif line[0] in HBNBCommand.classmodel and line[1] != d:
            print("** no instance found **")
        else:
            print("display instance")

        FileStorage().search(arg)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
