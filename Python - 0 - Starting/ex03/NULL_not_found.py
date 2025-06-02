def NULL_not_found(object: any) -> int:
    """
    Function that prints the object type of all types of "Null".
    Returns 0 if the object is a null-like value, 1 otherwise.
    """
    import math

    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
        return 0
    elif obj_type is float and math.isnan(object):
        print(f"Cheese: {object} {obj_type}")
        return 0
    elif obj_type is bool and object is False:
        print(f"Fake: {object} {obj_type}")
        return 0
    elif obj_type is int and object == 0:
        print(f"Zero: {object} {obj_type}")
        return 0
    elif obj_type is str and object == "":
        print(f"Empty: {object} {obj_type}")
        return 0
    else:
        print("Type not Found")
        return 1
