#!/usr/bin/env python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

def findLongestLen(strings):
    max = 0
    for string in strings:
        if len(string) > max:
            max = len(string)
    return max;

longestLengths = []
for list in tableData:
    longestLength = findLongestLen(list)
    longestLengths.append(longestLength)

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        list = tableData[j]
        item = list[i]
        print(item.rjust(longestLengths[j]), end=' ')
    print()

