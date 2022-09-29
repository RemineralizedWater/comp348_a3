def lucas_gen(seq):
    return list(dict.fromkeys(seq))


if __name__ == '__main__':
    print(lucas_gen(["apple", "banana", "cherry", "cherry"]))
