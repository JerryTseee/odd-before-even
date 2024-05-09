def solution(array):
    i = 0
    for j in range(len(array)):
        #if j is an odd
        if array[j] % 2 != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
    return array

array = [1,232,4,2,3,4,5,6,7,6,9]
print(solution(array))