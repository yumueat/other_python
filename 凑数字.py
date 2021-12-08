def way(a,b,s):
    i = j = 1
    a1 = s // a
    b1 = s // b
    for i in range(1, a1):
        for j in range(1, b1):
            if i * a + j * b == s:
                print("%s*%s+%s*%s=%s" % (i, a, j, b, s))


def main():
    while True:
        s = int(input("请输入总价:"))
        a, b = map(int, input("请输入单价:").split())
        way(a, b, s)
    pass

if __name__ == '__main__':
    main()