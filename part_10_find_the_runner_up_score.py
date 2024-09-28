if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_list = list(arr)
    arr_list.sort(reverse=True)
    max_arr_list = max(arr_list)
    while max_arr_list in arr_list:
        arr_list.pop(0)
    print(arr_list[0])
    
    
