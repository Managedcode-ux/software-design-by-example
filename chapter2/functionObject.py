import math


def square_perimeter(thing):
    return 4 * thing['side']


def square_area(thing):
    return thing['side'] ** 2


def square_larger(thing, size):
    return call(thing, "area") > size


def circle_perimeter(thing):
    return 2 * math.pi * thing['radius']


def circle_area(thing):
    return math.pi * thing['radius'] ** 2


def circle_larger(thing, size):
    return call(thing, "area") > size


def shape_density(thing, weight):
    return weight/call(thing, "area")


Shape = {
    "density": shape_density,
    "_classname": "Shape",
    "_parent": None,
}

Square = {
    "perimeter": square_perimeter,  # method
    "area": square_area,  # method
    "larger": square_larger,  # method
    "_classname": "Square",
    "_parent": Shape
}

Circle = {
    "perimeter": circle_perimeter,  # method
    "area": circle_area,  # method
    "larger": circle_larger,  # method
    "_classname": "Circle",
    "_parent": Shape
}


def square_new(name, side):
    return {
        "name": name,  # parameter
        "side": side,  # parameter
        "_class": Square
    }


def circle_new(name, radius):
    return {
        "name": name,  # parameter
        "radius": radius,  # parameter
        "_class": Circle
    }


def find(cls, method_name):
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError("method_name")


def call(thing, method_name, *args):
    method = find(thing["_class"], method_name)
    # return thing["_class"][method_name](thing, *args)
    return method(thing, *args)


examples = [square_new("sq", 2), circle_new("ci", 3)]
for ex in examples:
    name = ex["name"]
    p = call(ex, "perimeter")
    a = call(ex, "area")
    la = call(ex, "larger", 10)
    d = call(ex, "density", 5)
    print(f"{name} {p:.2f} {a:.2f}")
    print(f"is {ex['name']} larger? {la}")
    print(f"{name}: {d:.2f}")
