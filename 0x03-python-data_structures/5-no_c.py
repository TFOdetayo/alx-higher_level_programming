#!/usr/bin/python3
def no_c(my_string):
    result = []
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            result.append(letter)
    return ''.join(result)

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
