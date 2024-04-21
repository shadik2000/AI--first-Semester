# Custom exceptions
class ErrorA(Exception):
    pass

class ErrorB(Exception):
    pass

class ErrorC(Exception):
    pass

def f(x: int):
    try:
        g(x)
        print("f1")
    except ErrorA:
        print("f2")
    finally:
        print("f3")

def g(x: int):
    try:
        h(x)
        print("g1")
    except ErrorA:
        print("g2")
    except ErrorB:
        print("g3")
        if x < -10:
            raise ErrorC
            print("g4")
    
        else:
            print("g5")
        print("g6")

def h(x: int):
    try:
        if x > 10:
            raise ErrorA
        if x < 0:
            raise ErrorB
    finally:
        print("h1")
    print("h2")

with open("a5_ex4.txt", "w") as file:
    try:
        f(5)
        file.write("f(5) -> f1 g1 h1 h2 f3\n")
    except ErrorA:
        file.write("f(5) -> f2 g1 h1 h2 f3\n")
    except ErrorB:
        file.write("f(5) -> f3\n")

    try:
        f(-5)
        file.write("f(-5) -> f1 g1 h1 h2 f3\n")
    except ErrorA:
        file.write("f(-5) -> f2 g1 h1 h2 f3\n")
    except ErrorB:
        file.write("f(-5) -> f3\n")

    try:
        f(11)
        file.write("f(11) -> g1 h1 h2 f1 g5 f3\n")
    except ErrorA:
        file.write("f(11) -> g2 h1 h2 f3\n")
    except ErrorB:
        file.write("f(11) -> g3 h1 h2 f3\n")

    try:
        f(-11)
        file.write("f(-11) -> g1 h1 h2 f2 ErrorA\n")
    except ErrorB:
        file.write("f(-11) -> g3 h1 h2 f3\n")
    except ErrorC:
        file.write("f(-11) -> g4 h1 h2 f3\n")
