choose = int(input("enter a number betwen 1-3 to recieve a greeeting: "))

match choose:
    case 1:
        print("hello, good morning")
    case 2:
        print("hello, good afternon")
    case 3:
        print("hello good night")
    case _:
        print("invalid input")