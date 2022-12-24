#!/usr/bin/python3
def uppercase(str):
    for letr in str:
        letr = ord(letr)
        if letr >= 97 and letr <= 122:
            letr -= 32
            letr = chr(letr)
            print("{}".format(letr), end='')
            print("")
