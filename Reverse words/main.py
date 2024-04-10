def reverse_words(txt: str) -> str:
    result = ' '.join(lett[::-1] for lett in txt.split(' '))
    return result

if __name__ == "__main__":
    print(reverse_words("Hello world!"))
    print(reverse_words("Hello  world  double!"))