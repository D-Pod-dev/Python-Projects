def list_searcher(A: list[int], v: int) -> (int | None):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None