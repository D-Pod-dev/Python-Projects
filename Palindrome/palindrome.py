def palindrome(num: int) -> bool:
    num_by_digit = []

    while num > 0:
        num_by_digit.append(num%10)
        num //= 10
    
    num_by_digit = [int(digit) for digit in num_by_digit]
    return num_by_digit == list(reversed(num_by_digit))