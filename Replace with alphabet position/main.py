"""Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""

import string

def alphabet_position(text: str) -> str:
    lett = string.ascii_lowercase
    text = ''.join(text.split())
    result = [str(lett.index(x.lower())+1) for x in text if x.lower() in lett]
    return ' '.join(result)

if __name__ == "__main__":
    print(alphabet_position("The sunset sets at twelve o' clock."))
    print(alphabet_position("The narwhal bacons at midnight."))