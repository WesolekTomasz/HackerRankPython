def string(n):
    if 1 <= n <= 150:
        for x in range(1, n+1):
            print(x, end="")
    else:
        pass

if __name__ == '__main__':
    n = int(input())
    string(n)
    
