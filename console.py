#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


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

    def do_show(self, user_id):
        """
        print the string representation of an instance
        """
        # TODO: implement a check that only shows
        # matching class name
        # e.g show BaseModel <id>
        # TODO: to be discussed a bit too lengthy to type
        line = user_id.split(" ")
        d = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in HBNBCommand.classmodel:
            print("** class doesn't exist **")
        elif line[0] in HBNBCommand.classmodel and len(line) < 2:
            print("** instance id missing **")
        storage.reload()
        ret_dict = storage.all()
        for single_dict in ret_dict.values():
            ret_id = getattr(single_dict, "id")
            if ret_id == line[1]:
                print(single_dict)
                break
        else:
            print("** no instance found **")
    
    def do_destroy(self, user_id):
        line = user_id.split(" ")
        dict_cpy = {}
        # TODO: Add all the required checks
        # TODO: How do i update the JSON file to reflect the deleted instance ?
        storage.reload()
        ret_dict = storage.all()
        for single_dict in ret_dict.values():
            ret_id = getattr(single_dict, "id")
            if ret_id == line[1]:
                dict_cpy = single_dict.__dict__.copy()
                for key, value in dict_cpy.items():
                    delattr(single_dict, key)
                    return True
        else:
            print(" no instance found")

    def do_all(self, line):
        # TODO: yet to implement where "do_all" only
        # returns matching class name
        # e.g all BaseModel should only return
        # BaseModel objects.
        # Right now it returns all the objects

        # TODO: the all method is missing checks
        storage.reload()
        ret_dict = storage.all()
        for single_dict in ret_dict.values():
            print(single_dict)

    def do_update(self, user_args):
        user_args = user_args.splt(" ")
        dict_cpy = {}
        # TODO: Missing all the required checks
        storage.reload()
        ret_dict = storage.all()
        for single_dict in ret_dict.values():
            ret_id = getattr(single_dict, "id")
            if ret_id == user_args[1]:
                setattr(single_dict, user_args[2], user_args[3])
                dict_cpy = single_dict.__dict__.copy()
                dict_cpy["created_at"] = dict_cpy["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
                dict_cpy["updated_at"] = dict_cpy["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
                BaseModel(**dict_cpy)
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
