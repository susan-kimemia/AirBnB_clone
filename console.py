#!/usr/bin/python3
"""contains the command intepreter"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
import re


class HBNBCommand(cmd.Cmd):
    """command line shell interepreter"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Bypass empty line."""
        pass

    def do_EOF(self, line):
        '''
        exits the shell
        '''
        print()
        return True

    def precmd(self, line):
        """edits line b4 executing"""

        if '.' in line and ('(' in line and ')' in line):
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            line = line.split()
            line[1], line[0] = line[0], line[1]
            try:
                # removes quotation arround id
                line[2] = line[2].replace('"', '').replace("'", '')
                line[2] = line[2].replace(',', '')

                # protects the commas in the dict
                if not ('{' in line[3] or '}' in line[3]):
                    line[3] = line[3].replace('"', '').replace("'", "")
                    line[3] = ' '.join(line[3:])
                    line[3] = line[3].replace(',', '')
                    line = line[:4]
            except IndexError:
                pass
            line = ' '.join(line)
            return cmd.Cmd.precmd(self, line)
        else:
            return cmd.Cmd.precmd(self, line)

    def onecmd(self, line):
        """edits line"""

        if '.' in line and ('(' in line and ')' in line):
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            line = line.split()
            line[1], line[0] = line[0], line[1]
            try:
                # removes quotation arround id
                line[2] = line[2].replace('"', '').replace("'", '')
                line[2] = line[2].replace(',', '')

                # protects the commas in the dict
                if not ('{' in line[3] or '}' in line[3]):
                    line[3] = line[3].replace('"', '').replace("'", "")
                    line[3] = ' '.join(line[3:])
                    line[3] = line[3].replace(',', '')
                    line = line[:4]
            except IndexError:
                pass
            line = ' '.join(line)
            return cmd.Cmd.onecmd(self, line)
        else:
            return cmd.Cmd.onecmd(self, line)

    def do_quit(self, line):
        '''
Quit command, exit program
        '''
        return True

    def do_create(self, line):
        '''
Creates a new instance of BaseModel, saves it to the JSON file
and prints the id
        '''

        if not line:
            print("** class name missing **")
            return
        '''retrieve class name as key'''
        class_objects = storage.Classes()
        if line in class_objects:
            '''retrieve class object'''
            class_obj = class_objects[line]
            '''instance'''
            obj = class_obj()
            obj.save()
            print(obj.id)
            del obj
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''Prints the string rep of an instance
based on the class name and id'''
        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]
            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            if len(lines) < 2:
                print("** instance id missing **")
                return
            else:
                id_ = lines[1]

                key = "{}.{}".format(class_name, id_)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    obj = storage.Classes()[class_name](**obj)
                    print(obj)

    def do_destroy(self, line):
        """
Deletes an instance based on the class name and id
Usage: destroy [Class] [id]
        """
        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]

            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            if len(lines) < 2:
                print("** instance id missing **")
                return
            else:
                id_ = lines[1]
                key = "{}.{}".format(class_name, id_)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        '''Prints all string rep of all instances based or
not class name'''
        all_models = []

        if line:
            lines = line.split(' ')
            class_name = lines[0]

            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            else:
                key_iterator = iter(storage.all())
                while True:
                    try:
                        key, value = next(key_iterator)
                        if class_name in key:
                            # each matching  model
                            mo = storage.Classes()[class_name](**value)
                            all_models.append(str(mo))
                    except StopIteration:
                        break
        else:
            key_iterator = iter(storage.all())
            while True:
                try:
                    key, value = next(key_iterator)
                    class_name = key.split('.')[0]
                    all_models.append(str(storage.Classes()[class_name](
                        **value)))
                except StopIteration:
                    break
        print(all_models)

    def do_update(self, line):
        """
Updates an instance attribute.
        """

        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]

            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            if len(lines) < 2:
                print("** instance id missing **")
                return
            if class_name + '.' + lines[1] not in storage.all():
                print("** no instance found **")
                return
            if len(lines) < 3:
                print("** attribute name missing **")
                return
            # Extracts Dictionary if there is on
            if '{' in lines[2] and type(eval(' '.join(lines[2:]))) is dict:
                new_values = eval(' '.join(lines[2:]))

                iter_items = iter(new_values.items())
                while True:
                    try:
                        key, value = next(iter_items)
                        if key not in ("id", "created_at", "updated_at"):
                            storage.all()[class_name + '.' + lines[1]][key] = \
                                    value
                    except StopIteration:
                        break
                storage.save()
            else:
                if len(lines) < 4:
                    print("** value missing **")
                    return

                key = class_name + '.' + lines[1]
                if lines[2] not in ('updated_at', 'created_at', 'id'):
                    storage.all()[key].update({lines[2]: eval(lines[3])})
                    storage.save()

    def do_count(self, line):
        """Counts Number of Class Instance"""
        count = 0
        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]
            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return

        key_iterator = iter(storage.all())
        while True:
            try:
                key = next(key_iterator)
                if class_name in key:
                    count += 1
            except StopIteration:
                break

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
