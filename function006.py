animals = str(input("Type a valid animal [pig/duck/cat/dog]: "))


def speak(animals):
    if animals == "pig":
        return "oink"
    elif animals == "duck":
        return "quack"
    elif animals == "cat":
        return "meow!"
    elif animals == "dog":
        return "woof"
    else:
        return "woof"


print(speak(animals))
