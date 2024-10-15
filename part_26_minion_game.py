def minion_game(string):
    arr = []
    for i in string:
        if i.lower() in "aeiou":
            index = int(string.index(i))
            arr.append(string[index:])    
    print(arr)       
    
        

if __name__ == '__main__':
    s = input()
    minion_game(s)