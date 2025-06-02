ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set.discard("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

"""
What's happening in this code?

We're playing with Python's main data types and changing their values:

LIST (ft_list):
- Lists are like boxes you can modify - you can change what's inside
- Just use [index] to grab and change an item
- Here we swap "tata!" with "World!" at position 1

TUPLE (ft_tuple):
- Tuples are locked boxes - once made, you can't change what's inside
- So we just make a completely new tuple to "change" it
- Out with ("Hello", "toto!"), in with ("Hello", "France!")

SET (ft_set):
- Sets are like bags of unique items - no duplicates allowed
- Order doesn't matter, items can be shuffled around
- We kick out "tutu!" with discard() and toss in "Paris!" with add()

DICTIONARY (ft_dict):
- Dictionaries are like labeled boxes - each value has a key
- Change values by using their key like dict[key] = new_value
- We update "Hello"'s value from "titi!" to "42Paris!"

Then we just print everything to see our changes!
"""
