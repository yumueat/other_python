import sys
sys.setrecursionlimit(1002)
def rec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return 9*rec(n-1) + 10**(n-1)

def main():
    # IF(ISBLANK(B3), 0, 1) +
    temp =""
    for i in range(3,51):
        temp1 = "IF(ISBLANK(B"+str(i)+"), 0, 1) +"
        temp += temp1
    print(temp)
if __name__ == '__main__':
    main()