#!/usr/bin/python3

"""
This module contains a  base class for other classes of this project.
The goal of this base class is to manage id attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs).
"""
import json
import csv
import turtle


class Base:
    """This is the base class for other classes
    Attributes:

            Fields:
                __nb_objects
                id: Public instance attribute

            Methods:
                __init__(self, id=None)
                __nb_objects: Private class attribute
                to_json_string(list_dictionaries)
                from_json_string(json_string)
                save_to_file(cls, list_objs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instances"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of
        list of dictionaries I.e serializing lists of dict
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation I.e
        deserializing Json string back to object
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list of instances
        to a file
        """
        obj_arr = []
        if list is not None:
            for obj in list_objs:
                obj_arr.append(cls.to_dictionary(obj))

        my_file = cls.__name__ + ".json"
        with open(my_file, 'w', encoding="utf-8") as f:
            serialized = cls.to_json_string(obj_arr)
            f.write(serialized)

    @classmethod
    def load_from_file(cls):
        """Convert json content to instances and return list
        of instances
        """
        my_file = cls.__name__ + ".json"
        list_obj = []

        try:
            with open(my_file, encoding="utf-8") as f:
                obj = cls.from_json_string(f.read())
            for i, d in enumerate(obj):
                list_obj.append(cls.create(**obj[i]))

        except FileNotFoundError:
            pass

        return list_obj

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        i.e convert dictionary back to instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4, 5)
        if cls.__name__ == "Square":
            dummy = cls(4, 3, 7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in CSV and save to a file"""
        my_file = cls.__name__ + ".csv"

        with open(my_file, 'w', newline='') as f:
            writer = csv.writer(f)

            for obj in list_objs:
                if cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize in CSV"""
        obj_arr = []
        my_file = cls.__name__ + ".csv"

        with open(my_file, 'r', newline='') as f:
            reader = csv.reader(f)

            for row in reader:
                if cls.__name__ == "Square":
                    obj = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                            }
                if cls.__name__ == "Rectangle":
                    obj = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                            }
                obj_arr.append(cls.create(**obj))

        return obj_arr

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the rectangle and the square using turtle module

        Args:
            list_rectangle: List of rectangle objects
            list_squares: List of square objects
        """
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b6578f")
        tur.pensize(2)
        tur.shape("square")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for i in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()
            tur.color("#e8543f")

        for sqr in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(sqr.x, sqr.y)
            tur.down()
            for i in range(2):
                tur.forward(sqr.width)
                tur.left(90)
                tur.forward(sqr.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
