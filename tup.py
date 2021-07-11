def minmax(items):
    min = max = None
    for item in items:
        if min == None or item < min:
            min = item
        if max == None or item > max:
            max = item
    return (min,max)

min, max = minmax([5,3,7,2,1])
print('min: ',min,', max: ',max, sep='')

