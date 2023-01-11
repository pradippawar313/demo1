number = [1,2,2,3,3,4,4,5,5,6,7,7,7,2,3,4,6]
res = {}
for i in number:
    res[i] = number.count(i)
print(res)