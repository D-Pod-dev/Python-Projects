def merge(A: list[int], p: int, q: int, r: int):
    if A:
        
        merge_half1 = A[p:q+1]
        merge_half2 = A[q+1:r+1]
        merged = []

        while (len(merge_half1) and len(merge_half2)):
            if merge_half1[0] <= merge_half2[0]:
                merged.append(merge_half1.pop(0))
            else: #if merge_half2[0] < merge_half1[0]
                merged.append(merge_half2.pop(0))

        merged += merge_half1 if merge_half1 else merge_half2

        for i in range(p, r+1):
            del A[i]
            A.insert(i, merged.pop(0))
        
    return A

# merge([7,9,0,2,4,1,3,8,6], 2, 4, 6)
merge([], 0, 0, 0)