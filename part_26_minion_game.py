def minion_game(string):
    arr = []
    count_number = 0
    for i in string:
        x = string.index(i)
        string = string[(x):]
        if i.lower() in "aeiou":
            for i in range(len(string)):
                if i != 0:
                    arr.append(string[:-i])
                else:
                    arr.append(string)
    for items in arr:
        x = arr.count(items)
        count_number += x
        

        
    print(arr)
    
        

if __name__ == '__main__':
    s = input()
    minion_game(s)