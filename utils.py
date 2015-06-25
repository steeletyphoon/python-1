"""This is my awesome utility kitchen sink. Don't judge me."""
import colors as c

def ask(question):
    print(question)
    answer = input('>' + c.base3)
    answer = answer.lower().strip()
    print(c.reset)
    return answer
