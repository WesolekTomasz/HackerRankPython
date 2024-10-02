def mutate_string(string, position, charakter):
    arr = list(string)
    arr[position] = charakter
    string = ''.join(arr)
    return string    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)