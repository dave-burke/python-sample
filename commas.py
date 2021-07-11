import copy

spam = ['apples', 'bananas', 'tofu', 'cats']

for i in range(len(spam)):
    if i != 0:
        print(', ', end='')
    if i == len(spam) - 1:
        print('and ', end='')
    print(spam[i], end='')
print()
