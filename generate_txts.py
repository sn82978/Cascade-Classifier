import os

NEGDIR = "/home/drosophila-lab/Documents/Fecundity/Haar-Cascade/n"

def make_negative_txt():
    with open('n.txt', 'w')  as file:
        for filename in os.listdir(NEGDIR):
            file.write(f"n/{filename}\n")

def make_positive_txt():
    # reconstruct imgs
    # find where the bounding boxes coors are (4)
    # needs to be in format of p/filename 1coor1 1coor2 1coor3 1coor4   2coor1 2coor2 2coor3 2coor4
    pass