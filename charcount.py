def charcount(str):
    result = {}
    for c in str:
        result.setdefault(c, 0)
        result[c]+=1
    return result

def display_result(dict):
    for k,v in dict.items():
        print(f'{k} appeared {v} times')

display_result(charcount('It was a bright cold day in April, and the clocks were striking thirteen.'))
