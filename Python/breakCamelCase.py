"""Complete the solution so that the function will break up camel casing, using a space between words."""
def solution(s):
    result = ""
    for char in s:
        if char.isupper(): 
            result += " "
        result += char
    return result