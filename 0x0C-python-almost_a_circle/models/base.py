#!/usr/bin/python3
"""
1. Base class
"""
import json
import os
import csv


class Base:
    """
    create the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """"returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        str_rep = json.dumps(list_dictionaries)
        return str_rep

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        list_rep = json.loads(json_string)
        return list_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inherits of Base
        """
        if not list_objs:
            with open(f"{cls.__name__}.json", 'w') as file:
                file.write("[]")
        else:
            dict_list = []
            for object in list_objs:
                dict_list.append(object.to_dictionary())

            with open(f"{cls.__name__}.json", 'w') as file:
                file.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Update the class Base by adding the class method
        that returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        list_of_dict = cls.from_json_string(json_string)
        instances = [cls.create(**dic) for dic in list_of_dict]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes objects to CSV file."""
        if not list_objs:
            with open(f"{cls.__name__}.csv", "w") as file:
                file.write("[]")
            return

        # Determine CSV headers based on class
        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            attrs = ["id", "size", "x", "y"]

        # Write each object as a CSV line
        with open(f"{cls.__name__}.csv", "w") as file:
            for obj in list_objs:
                # Get attributes in order (e.g., obj.id, obj.width, etc.)
                csv_line = ",".join(str(getattr(obj, attr)) for attr in attrs)
                file.write(csv_line + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file.

        Returns:
            list: A list of Rectangle or Square instances
            loaded from the CSV file.
            Returns an empty list if the file doesn't exist.
        """
        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []

        instances = []

        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if not row:  # Skip empty lines
                    continue

                try:
                    # Convert all values to integers
                    values = [int(value) for value in row]

                    if cls.__name__ == "Rectangle":
                        if len(values) == 5:
                            # id, width, height, x, y
                            instance = cls(values[1], values[2],
                                           values[3], values[4], values[0])
                            instances.append(instance)
                    elif cls.__name__ == "Square":
                        if len(values) == 4:
                            # id, size, x, y
                            instance = cls(values[1], values[2],
                                           values[3], values[0])
                            instances.append(instance)

                except (ValueError, IndexError):
                    # Skip rows with invalid data
                    continue

        return instances
