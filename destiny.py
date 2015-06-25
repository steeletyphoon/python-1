"""The Destiny Quiz Module."""

import colors as c
from utils import ask

intro = c.clear + c.blue + '''
Welcome to the Destiny adventure quiz...
''' + c.reset

def q1():
    answer = ask(c.base3 + "What is the first gun that you get?")
    if answer == "khovostav":
        return True
    return False
def q2():
    answer = ask(c.red + "Who is the house of wolves leader?")
    if answer.startswith("skolas"):
        return True
    return False
def q3():
    answer = ask(c.blue + "What is the best class?")
    if answer.startswith("not titan"):
        return True
    return False
def q4():
    answer = ask(c.orange + "What two types of damage does the Gjallarhorn do?")
    if answer.startswith("solar and arch"):
        return True
    return False
def q5():
    answer = ask(c.yellow + "When is Xur actually useful?")
    if answer.startswith("never"):
        return True
    return False
def q6():
    answer = ask(c.green + "What is the number one gun used in Trials of Osiris?")
    if answer.startswith("thorn"):
        return True
    return False
def q7():
    answer = ask(c.base00 + "What is the handcannon that is a playstation exclusive before the Taken Kings release?")
    if answer.startswith("hawkmoon"):
        return True
    return False
def q8():
    answer = ask(c.base01 + "What is the helmet that blinds enemy's when inside the titan bubble?")
    if answer.startswith("helm of saint-14"):
        return True
    return False
def q9():
    answer = ask(c.base02 + "What is the helmet that when you use a nova bomb, how many kills that you get helps you get your super back?")
    if answer.startswith("obsidian mind"):
        return True
    return False
def q10():
    answer = ask(c.orange + "What is the helmet that allows you to have a 6x golden gun shot with keyhole?")
    if answer.startswith("celestial nighthawk"):
        return True
    return False
def q11():
    answer = ask(c.red + "True or False, Crucible is a fair and fun mode for destiny players.")
    if answer.startswith("False"):
        return True
    return False

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11]
