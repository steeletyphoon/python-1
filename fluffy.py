"""The pink fluffy unicorn quiz module."""

import colors as c
from utils import ask

intro = c.clear + c.magenta + '''
Welcome to the Pink Fluffy Unicorns quiz.
Let's test your knowledge...
''' + c.reset

def q1():
    answer = ask(c.magenta + "What color are the unicorns?")
    if answer == "pink":
        return True
    return False
def q2():
    answer = ask(c.magenta + "What are the unicorns dancing on?")
    if answer.startswith("rainbow"):
        return True
    return False
def q3():
    answer = ask(c.magenta + "Use one word to describe the texture of their magical fur.")
    if answer.startswith("smile"):
        return True
    return False

questions = [q1,q2,q3]
