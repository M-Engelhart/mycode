#!/usr/bin/env python3
## create file object in "r"ead mode
file = input("What file do you want to load? : ")
with open(file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    linecount = 0
    for line in configfile:
        configlist = configfile.readlines()
        linecount += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(linecount)
