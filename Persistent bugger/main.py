def mulDigit(n: int) -> int:
    if n < 10:
        return n
    return n%10 * mulDigit(n//10)

def persistence(n: int) -> int:
    if n < 10:
        return 0
    return 1 + persistence(mulDigit(n))


if __name__ == '__main__':
    print(persistence(39))
    print(persistence(999))
    print(persistence(4))