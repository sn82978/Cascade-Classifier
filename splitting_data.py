import os
# import opencv
import re
import shutil

DATAPATH = "/home/drosophila-lab/Documents/Fecundity/04-30-cap-800x800-sliced-Alexander"
POSDIR = "/home/drosophila-lab/Documents/Fecundity/Cascade-Classifier/p/"
NEGDIR = "/home/drosophila-lab/Documents/Fecundity/Cascade-Classifier/n/"

# split zeros into n, and the rest is p

for file in os.listdir(DATAPATH):
    imgpath = os.path.join(DATAPATH, file)
    print(imgpath)
    x = re.search("eggs[0-9]", file)
    egg_count_str = re.search("[0-9]", x.group())
    if egg_count_str.group() == "0":
        print(f"negative folder: {file}")
        #os.rename(imgpath, f"{NEGDIR}{file}")
        #os.replace(imgpath, f"{NEGDIR}{file}")
        shutil.move(imgpath, f"{NEGDIR}{file}")
    else:
        print(f"positive folder: {file}")
        #os.rename(imgpath, f"{POSDIR}{file}")
        #os.replace(imgpath, f"{POSDIR}{file}")
        shutil.move(imgpath, f"{POSDIR}{file}")

