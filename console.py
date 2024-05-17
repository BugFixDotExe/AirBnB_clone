#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "
    classmodel = {"BaseModel":BaseModel, "User":User}

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        print("")
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_create(self, arg):
        if len(arg) ==  0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classmodel:
            print("** class doesn't exist **")
        else:
            print("you can create instance")
            new_instance = HBNBCommand.classmodel[arg]()
            #with open("filename.json", "w", encoding = "UTF-8") as F_obj:
             #   dump(self.__file_path, F_obj)
            print("save")
            print(new_instance.id)
    def do_show(self, arg):
        pass
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
