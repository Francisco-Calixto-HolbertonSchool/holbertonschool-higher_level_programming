#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    names = dir()
    for i in range(len(names)):
        if names[i][0:2] != "__":
            print(names[i])
