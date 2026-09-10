def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw, val in keywords.items():
        print(kw, ":", val)


def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def customFn(ham: str, eggs: str = "eggs") -> str:
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs


cong = lambda x, y: x + y

cheeseshop(
    "Limburger",
    "This is arg 1",
    "this is arg 2",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
)

# invalid calls
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
print("\n========================\n")
# valid calls
parrot(1000)
print("\n========================\n")
print(cong(1, 2))
print("\n========================\n")
print("Annotations:", customFn.__annotations__)
print("\n========================\n")
print(f"{list('hello')}")

number = (x for x in "hello")

while True:
    temp = next(number, None)
    if temp == None:
        break
    print(temp)

print("\n========================\n")
t1 = 12, 3, "hai"
t2 = (1, 2, 3)
print((t1, t2))
print(type((t1, t2)))

# a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective
singleton = ("hello",)  # <-- note trailing comma
print(singleton)
print(type(singleton))

print("\n========================\n")
print(dict([("sape", 4139), ("guido", 4127), ("jack", 4098)]))  # noqa: C406
