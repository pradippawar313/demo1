from collections import Counter
number = [1,2,2,3,3,4,4,5,5,6,7,7,7,2,3,4,6]
counts = dict(Counter(number))
duplicate = {key:value for key,value in counts.items() if value > 1}
print(duplicate)
