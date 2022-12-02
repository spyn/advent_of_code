import os
# data = 'https://adventofcode.com/2022/day/1/input' (ergh proxy, saving file locally)

i=1; elvenTotal=0; elven={}

with open('1.txt') as f:    
    for line in f:
        if not line.rstrip():
            elven[i] = elvenTotal; elvenTotal = 0; i = i+1; next
        else:
            elvenTotal = elvenTotal + int(line.rstrip())

print(sorted(elven.items(), key=lambda item: item[1], reverse=True)[:1])