#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for letter in my_string:
        if letter not in 'cC':
            result += letter
    return result

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
