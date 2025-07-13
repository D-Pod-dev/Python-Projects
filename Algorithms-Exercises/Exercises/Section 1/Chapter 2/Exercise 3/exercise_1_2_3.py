def rep_occurences_searcher(A: list[int], v: int) -> bool:
    occurences = 0
    for x in A:
        if x == v:
            occurences += 1
        if occurences > 1:
            return True
    return False