def lucas_gen(n):
    a, b = 2, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(lucas_gen(5)))
