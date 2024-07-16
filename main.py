import random


def print_statement(text):
    print(text)
    
def get_random():
    return random.randint(0, 11)


def get_name():
    return "Usama Bashir"

if __name__ == '__main__':
    name = get_name()
    print_statement(name)
    print(get_random())
