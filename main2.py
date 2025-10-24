def merge_arrays(arrayA, arrayB):
    # 1: Merge arrayA and arrayB
    # 2: Remove duplicates
    # 3: Sort list in ascending order
    return sorted(set(arrayA + arrayB))
    
a = [1,2,3,4,5,6]
b = [4,4,5,6,7,8,9]
c = merge_arrays(a,b)
print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]