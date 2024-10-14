a = "abcdefghijklmnopqrstuwxyz"

def print_rangoli(lenght):
    lines = []
    for row in range(lenght):
        print_ = "-".join(a[row:lenght])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])

    for row in range(lenght-1, 0, -1):
        print(lines[row].center(width, '-'))

    for row in range(lenght):
        print(lines[row].center(width, '-'))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


