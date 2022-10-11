#!/usr/bin/python3

def reverse_string(text):
    # Recursive termination
    if len(text) <= 1:
        return text
    first_char = text[0]
    remaining = text[1:]

    # recursive descent
    return reverse_string(remaining) + first_char

string = reverse_string("Hello")
print(string)
