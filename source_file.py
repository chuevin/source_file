# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:49:51 2020

@author: chuev
"""

# Wrong way to source file in Python
# Because not all python libraries will work if you use wrong operating system.

data_folder = "Documents/test/"

file_to_open = data_folder + "testing1.txt"

f = open(file_to_open)

print(f.read())

# Right way to source file in Python 

from pathlib import Path
import webbrowser

filename = Path("Documents/test/testing1.txt")

webbrowser.open(filename.absolute().as_uri())

# pathlib methods

from pathlib import Path

filename = Path("Documents/test/testing.txt")

print(filename.name)
# prints "testing1.txt"

print(filename.suffix)
# prints "txt"

print(filename.stem)
# prints "testing

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")