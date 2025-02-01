import os

NEGDIR = "./n"
POSDIR = "./p"

def make_negative_txt():
    with open('n.txt', 'w')  as file:
        for filename in os.listdir(NEGDIR):
            file.write(f"n/{filename}\n")

def make_positive_txt():
    with open('p.txt', 'w')  as file:
        for filename in os.listdir(POSDIR):
            file.write(f"p/{filename}\n")

if __name__ == '__main__':
    make_positive_txt()