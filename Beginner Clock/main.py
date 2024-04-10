"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59"""

def past(h: int, m: int, s: int) -> int:
    return (h*60**2 + m*60 + s)*1000

if __name__ == "__main__":
    print(past(0, 1, 1))
    print(past(1, 1, 1))
    print(past(0, 0, 0))
    print(past(1, 0, 1))