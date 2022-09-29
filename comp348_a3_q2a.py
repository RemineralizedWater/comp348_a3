def lucas_loop(n):
    a, b = 2, 1
    lucas_list = []
    for _ in range(n):
        lucas_list.append(a)
        a, b = b, a + b
    print(lucas_list)


if __name__ == '__main__':
    lucas_loop(4)
