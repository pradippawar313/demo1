def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i - 1 ):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data = [-4,6,0,5,-2,7,8,9]
bubblesort(data)
print("sorted array in asending order : ")
print(data)