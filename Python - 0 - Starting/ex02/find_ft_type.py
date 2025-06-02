def all_thing_is_obj(object: any) -> int:
    """
    Function that prints the object type and returns 42.

    Args:
        object: any type of object to analyze

    Returns:
        int: always returns 42
    """
    obj_type = type(object)

    if obj_type is None:
        print(f"Nothing : {object} {obj_type}")
    if obj_type is list:
        print(f"List : {obj_type}")
    elif obj_type is tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type is set:
        print(f"Set : {obj_type}")
    elif obj_type is dict:
        print(f"Dict : {obj_type}")
    elif obj_type is str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
