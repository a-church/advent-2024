lines_combined = '''3   4
4   3
2   5
1   3
3   9
3   3'''

raw = list(map(int, lines_combined.split()))

list1 = raw[::2]
list2 = raw[1::2]
list1.sort(), list2.sort()

distance = 0

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)