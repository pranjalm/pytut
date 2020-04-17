# solution for https://www.hackerrank.com/challenges/nested-list/problem
a = {}
b = set()
n = int(input())
for i in range(n):
    name = input() #key
    score = float(input()) #value
    a.update({name:score})
    b.add(score)
b = list(b)
b = sorted(b)
b = b[1]
e = []
for i,j in a.items():
    if(j==b):
        e.append(i)
    else:
        continue

e = sorted(e)
#print(a,b,e)
for i in e:
    print(i)
