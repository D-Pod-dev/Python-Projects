def binary_addition(A: list[int], B: list[int]) -> list[int]:
    A.reverse()
    B.reverse()
    C = [0]

    g_arr_len = len(A) if (len(A) >= len(B)) else len(B)

    for i in range(g_arr_len):

        if (i + 1) > len(A):
            A.append(0)
        elif (i + 1) > len(B):
            B.append(0)

        s = int((A[i] or B[i]) and not (A[i] and B[i]))

        r = int(A[i] and B[i])

        v = C[i]

        C[i] = int((v or s) and not (v and s))

        p = int(v and s)

        C.append(int(p or r))
    
    C.reverse()
    return C