#VL 2nd period *args and **kwargs

"""def hello(name="Tia", age=29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello("Xavier"))
print(hello(age = 19, name="Treyson"))"""

# positional arguements, *args, Keyword arguements, **kwargs
def hello(*names, **last):
    print(type(names))
    print(last)
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['vlast']} ")
        else:
            print(f"Hello {name} {last['alast']}")

hello("Alexander", "Kathryn", "Andrew", "Vienna", "Victoria", "Treyson", "Xavier", "Jake", alast = "LaRose", vlast="Atkin")