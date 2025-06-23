#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)

try:
    r.y = -12
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.y = -89
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.y = -1
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.y = 0
    print("OK", end="")
except Exception as e:
    print("0 is valid for y: [{}] {}".format(type(e), e))
    exit(1)
